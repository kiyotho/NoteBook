from PySide6.QtWidgets import QApplication
import sys
from widget import NoteBook

app = QApplication(sys.argv)

window = NoteBook(app)
window.show()

app.exec()
