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

with open("notes_data.json", "r", encoding='UTF-8') as file:
    NOTES = json.load(file)

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

        NOTES[note_name]["текст"] = note_text

        with open("notes_data.json", "w", encoding='UTF-8') as file:
            json.dump(NOTES, file)
ui.save_note.clicked.connect(save_note)

def del_note():
    if ui.notes_list.selectedItems():
        note_name = ui.notes_list.currentItem().text()

        del NOTES[note_name]
    
        ui.textEdit.clear()

        ui.notes_list.clear()
        ui.notes_list.addItems(NOTES)

        with open("notes_data.json", "w", encoding="UTF-8") as file:
            json.dump(NOTES, file)

ui.btn_delette_note.clicked.connect(del_note)

def add_tag():
    if ui.notes_list.selectedItems():
        if ui.tag_search.text():
            note_name = ui.notes_list.currentItem().text()
            new_tag = ui.tag_search.text()
            if not new_tag in NOTES[note_name]["теги"]:
                NOTES[note_name]["теги"].append(new_tag)

                ui.tags_list.addItem(new_tag)
                ui.tag_search.clear()

                with open("notes_data.json", "w", encoding="UTF-8")as file:
                    json.dump(NOTES, file)
                    

ui.btn_add_tag.clicked.connect(add_tag)

def del_tag():
    if ui.notes_list.selectedItems():
        note_name = ui.notes_list.currentItem().text()
        if ui.tags_list.selectedItems():
            tag = ui.tags_list.currentItem().text()
            NOTES[note_name]["теги"].remove(tag)

            ui.tags_list.clear()
            ui.tags_list.addItem(NOTES[note_name]["теги"])
            with open("notes_data.json", "w", encoding="UTF-8")as file:
                json.dump(NOTES, file)

ui.btn_delete_tag.clicked.connect(del_tag)

def search_tag():
        tag = ui.tag_search.text()
        filtered_notes = {}
        for note_name, note in NOTES.items():
            if tag in note["теги"]:
                filtered_notes[note_name] = note

        ui.notes_list.clear()
        ui.notes_list.addItems(filtered_notes)

        ui.btn_search_tag.setText("скинути пошук")

    elif ui.btn_search_tag.text() == "Скинути пошук":
        ui.notes_list.clear()
        ui.notes_list.addItems(NOTES)
        ui.btn_search_tag.setText("Шукати по тегу")
        ui.tag_search.clear()


ui.btn_search_tag.clicked.connect(search_tag)

win.show()
app.exec()