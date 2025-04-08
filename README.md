# Alpha.BETa - Lernapp zur Bildung und Management eines Informationspools

## Beschreibung
Alpha.BETa ist eine Anwendung zur fachlichen Bildung und zum Vokabellernen. Die App ermoeglicht es Benutzern, "Lernkarten" fuer verschiedene Themen zu erstellen, Woerter hinzuzufuegen und Erklaerungen zu speichern. User koennen auch ein Quiz durchfuehren, um ihr Wissen zu testen und zu festigen.

## Funktionen
- **Themenmanagement**: Nutzer kann verschiedene Themen erstellen, auswaehlen und bearbeiten.
- **Woerterverwaltung**: Hinzufuegen, Bearbeiten und Loeschen von Woertern mit Erklaerungen.
- **Speicherung**: Woerter und Erklaerungen werden in einer JSON-Datei (`vocabulary.json`) gespeichert.
- **Quiz-Funktion**: Benutzer koennen sich nach dem Zufallprinzip abfragen lassen und die Dauer der Uebung festlegen.(Anzahl Woerter / alle Woerter).

## GUI
Die Benutzeroberflaeche basiert auf PyQt6 und besteht aus folgenden Komponenten:
- QApplication: laedt alle anderen GUI-Elemente
- QWidget: GUI-Objekte erstellen, z. B. das Hauptfenster der Anwendung.
- QVBoxLayout: Layout-Manager
- QPushButton: Knoepfe fuer Useraktionen
- QTextEdit: Mehrzeiliges Eingabefeld fuer die Erklaerungen.
- QMessageBox: Nachrichten / Fehlermeldungen anzeigen
- QListWidget: Liste fuer eingegebene Woerter, die man auswaehlen kann.
- QComboBox: Dropdownauswahl des Themas.
- QDialog: Eroeffnen von Dialogfenstern, z. B. zum Bearbeiten der Erklaerungen.
- QLabel: Anzeigen von statischem Text oder Informationen in der GUI.
- QFormLayout: Layout festlegen zur Anordnung von Feldern in einem Formular (z.B. beim Bearbeiten von Erklaerungstexten).
- QInputDialog: Dialog zur Eingabe von Text.

## Installation

1. **Python installieren**: Stelle sicher, dass Python 3.12 auf deinem Computer installiert ist. Du kannst Python von [python.org](https://www.python.org/downloads/) herunterladen.

2. **Virtuelle Umgebung einrichten**:
   ```bash
   cd Pfad/zum/Alpha.BETa
   python -m venv venv

Virtuelle Umgebung aktivieren:

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

Benoetigte Pakete installieren:

pip install PyQt6

Anwendung starten:

python vocabulary_app.py

## Nutzung der App

1.Erstelle ein Themengebiet oder waehle ein Thema aus dem Dropdown-Menue aus.
2.Fuege ein neues Wort und die dazugehoerige Erklaerung hinzu.
3.Du kannst das Wort auswaehlen, um die Erklaerung anzuzeigen oder zu veraendern.
Starte ein Quiz, um dein Wissen zu testen.

## Roadmap - kurz

Hier sind die Schritte, die ich zur Entwicklung der Alpha.BETa-Anwendung unternommen habe:

Funktionen festlegen
Gestaltung der GUI
Datenverwaltung
Quiz-Funktion
Fehlerbehebung und Optimierung
Dokumentation
Version 1.0 Veroeffentlichung auf GitHub

Diese Roadmap zeigt kurzgefasst die wichtigsten Schritte und Ueberlegungen, die waehrend der Entwicklung der Anwendung verfolgt wurden.

## Die volle Roadmap ist in der Datei Roadmap_1.0.PDF nachzuvollziehen

## Impressum

Entwickelt von Semenov Iaroslav , Fachinformatiker Anwendungsentwicklung , 1. Lehrjahr bei der BIB Augsburg GgmbH
