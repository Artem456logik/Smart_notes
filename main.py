from PyQt6.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)

NOTES = {
    "купи діда": {
        "текст": "не забудь купити діда на борщ"
        "теги" : ["покупка", "дід",],
    },
    "продай кота": {
        "текст": "не забудь продати кота"
        "теги": ["кіт", "sell",],
    }
}





win.show()
app.exec()