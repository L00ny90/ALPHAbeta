import sys
import json
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QMessageBox, QListWidget, QComboBox,
    QTextEdit, QDialog, QLabel, QFormLayout, QInputDialog
)
from PyQt6.QtGui import QIcon


class EditExplanationDialog(QDialog):
    def __init__(self, current_explanation, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Erklärung ändern")
        self.resize(300, 200)

        layout = QFormLayout()

        self.explanation_input = QTextEdit()
        self.explanation_input.setPlainText(current_explanation)
        layout.addRow(QLabel("Ändern Sie die Erklärung:"), self.explanation_input)

        self.save_button = QPushButton("Speichern")
        self.save_button.clicked.connect(self.accept)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def get_explanation(self):
        return self.explanation_input.toPlainText().strip()


class VocabularyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setGeometry(100, 100, 400, 300)

        # Setze das Icon für die Anwendung
        self.setWindowIcon(QIcon("icon.png"))

        self.vocab_dict = {}
        self.selected_topic = None

        self.initUI()
        self.load_data()

    def initUI(self):
        layout = QVBoxLayout()

        self.topic_combo = QComboBox()
        self.topic_combo.addItem("Thema auswählen")
        self.topic_combo.currentIndexChanged.connect(self.topic_selected)
        layout.addWidget(self.topic_combo)

        self.add_topic_button = QPushButton("Thema hinzufügen")
        self.add_topic_button.clicked.connect(self.add_topic)
        layout.addWidget(self.add_topic_button)

        self.word_input = QLineEdit(self)
        self.word_input.setPlaceholderText("Wort")
        layout.addWidget(self.word_input)

        self.explanation_input = QTextEdit(self)
        self.explanation_input.setPlaceholderText("Erklärung für das Wort")
        layout.addWidget(self.explanation_input)

        self.add_word_button = QPushButton("Wort hinzufügen")
        self.add_word_button.clicked.connect(self.add_word)
        layout.addWidget(self.add_word_button)

        self.word_list = QListWidget()
        self.word_list.itemClicked.connect(self.show_explanation)
        layout.addWidget(self.word_list)

        self.delete_button = QPushButton("Ausgewähltes Wort löschen")
        self.delete_button.clicked.connect(self.delete_word)
        layout.addWidget(self.delete_button)

        self.edit_button = QPushButton("Erklärung ändern")
        self.edit_button.clicked.connect(self.edit_explanation)
        layout.addWidget(self.edit_button)

        self.shuffle_button = QPushButton("Quiz starten!")
        self.shuffle_button.clicked.connect(self.start_quiz)
        layout.addWidget(self.shuffle_button)

        # Button für die Infobox
        self.info_button = QPushButton("Impressum")
        self.info_button.clicked.connect(self.show_info)
        layout.addWidget(self.info_button)

        self.setLayout(layout)

    def topic_selected(self):
        self.selected_topic = self.topic_combo.currentText()
        self.load_words()

    def add_topic(self):
        topic, ok = QInputDialog.getText(self, "Thema hinzufügen", "Geben Sie den Namen des Themas ein:")
        if ok and topic:
            self.topic_combo.addItem(topic)
            self.vocab_dict[topic] = {}
            self.save_data()

    def add_word(self):
        word = self.word_input.text().strip()
        explanation = self.explanation_input.toPlainText().strip()
        if word and explanation and self.selected_topic:
            self.vocab_dict[self.selected_topic][word] = explanation
            self.word_input.clear()
            self.explanation_input.clear()
            self.save_data()
            self.load_words()

    def load_words(self):
        self.word_list.clear()
        if self.selected_topic:
            words = sorted(self.vocab_dict[self.selected_topic].keys())
            self.word_list.addItems(words)

    def delete_word(self):
        selected_item = self.word_list.currentItem()
        if selected_item and self.selected_topic:
            word = selected_item.text()
            del self.vocab_dict[self.selected_topic][word]
            self.save_data()
            self.load_words()

    def show_explanation(self, item):
        word = item.text()
        explanation = self.vocab_dict[self.selected_topic][word]
        QMessageBox.information(self, word, explanation)

    def edit_explanation(self):
        selected_item = self.word_list.currentItem()
        if selected_item and self.selected_topic:
            word = selected_item.text()
            current_explanation = self.vocab_dict[self.selected_topic][word]

            dialog = EditExplanationDialog(current_explanation, self)
            if dialog.exec():
                new_explanation = dialog.get_explanation()
                if new_explanation:
                    self.vocab_dict[self.selected_topic][word] = new_explanation
                    self.save_data()
                    self.load_words()

    def start_quiz(self):
        if not self.selected_topic:
            QMessageBox.warning(self, "Fehler", "Bitte wählen Sie ein Thema aus.")
            return

        # Quiz Optionen abfragen
        quiz_type, ok = QInputDialog.getItem(self, "Quiz Optionen", "Wie möchten Sie das Quiz durchführen?",
                                             ["Alle Wörter abfragen", "Anzahl Wörter abfragen"], 0, False)

        if not ok:
            return  # Abbrechen, wenn der Benutzer nicht bestätigt

        if quiz_type == "Alle Wörter abfragen":
            self.ask_all_words()
        elif quiz_type == "Anzahl Wörter abfragen":
            self.ask_number_of_words()

    def ask_all_words(self):
        words = list(self.vocab_dict[self.selected_topic].items())
        random.shuffle(words)
        self.ask_words(words)

    def ask_number_of_words(self):
        num_words, ok = QInputDialog.getInt(self, "Anzahl Wörter abfragen", "Wie viele Wörter möchten Sie abfragen?",
                                            min=1, max=len(self.vocab_dict[self.selected_topic]))
        if ok:
            words = list(self.vocab_dict[self.selected_topic].items())
            random.shuffle(words)
            selected_words = words[:num_words]
            self.ask_words(selected_words)

    def ask_words(self, words):
        for word, explanation in words:
            reply = QMessageBox.question(self, word, "Erklärung anzeigen?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)
            if reply == QMessageBox.StandardButton.Yes:
                QMessageBox.information(self, word, explanation)
            elif reply == QMessageBox.StandardButton.Cancel:
                break  # Quiz vorzeitig beenden

    def show_info(self):
        info_text = (
            "Entwickler: Semenov Iaroslav\n"
            "Organisation: BIB Augsburg gGmbH\n"
            "Icons erstellt von Smashicons - Flaticon (https://www.flaticon.com/de/kostenlose-icons/online-lernen)\n"
            "Geschrieben in Python 3.12\n"
            "GUI: PyQt6\n"
            "IDE: PyCharm Community Edition 2024.2.1\n"
            "Version: v1.0\n"
            "Lizenz: Freeware"
        )
        QMessageBox.information(self, "Impressum", info_text)

    def save_data(self):
        with open('vocabulary.json', 'w', encoding='utf-8') as file:
            json.dump(self.vocab_dict, file, ensure_ascii=False, indent=4)

    def load_data(self):
        try:
            with open('vocabulary.json', 'r', encoding='utf-8') as file:
                self.vocab_dict = json.load(file)
                for topic in self.vocab_dict.keys():
                    self.topic_combo.addItem(topic)
        except FileNotFoundError:
            self.vocab_dict = {}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VocabularyApp()
    ex.show()
    sys.exit(app.exec())
