from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog

from ui import Ui_MainWindow
import json

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)

NOTES = {
    "купи йобнутого діда": {
        "текст": "не забудь купити діда на борщ ЩОБ ВІН ТВАРЬ ТУДА НАСРАВ",
        "теги" : ["покупка", "дід",],
    },
    "продай обдристаного кота": {
        "текст": "не забудь продати кота якого Їбали в сраку",
        "теги": ["кіт", "sell",],
    },
}

with open("notes_data.json", "w", encoding='UTF-8') as file:
    json.dump(NOTES, file)

with open("notes_data.json", "r", encoding='UTF-8') as file:
    NOTES = json.load(file)

for note in NOTES:
    ui.notes_list.addItem(note)

ui.notes_list.addItems(NOTES)

def show_note():
    note_name = ui.notes_list.selectedItems()[0].text()
    note = NOTES[note_name]
    ui.textEdit.setText(note["текст"])
    ui.tags_list.clear()
    ui.tags_list.addItems(note['теги'])
ui.notes_list.itemClicked.connect(show_note)

def addNote():
    note_name, ok = QInputDialog.getText(
        win, "Додати нлотатку", "Введіть назву нової нлотатки:"
    )
    if ok:
        NOTES[note_name] = {
            "текст":"",
            "теги":[]
        }
        ui.notes_list.addItem(note_name)
ui.btn_create_note.clicked.connect(addNote)

def save_note():
    if ui.notes_list.selectedItems():
        note_name = ui.notes_list.currentItem().text()
        note_text = ui.textEdit.toPlainText()

        NOTES[note_name] = {
            "текст": note_text,
            "теги": []
        }

        with open("notes_data.json", "w", encoding='UTF-8') as file:
            json.dump(NOTES, file)
ui.save_note.clicked.connect(save_note)

win.show()
app.exec()