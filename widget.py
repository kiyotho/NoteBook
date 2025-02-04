#importing essential ibraries
from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox, QToolBar, QTextEdit,  QStatusBar, QFileDialog, QDialog
from PySide6.QtCore import  Qt, QTimer
from PySide6.QtGui import QAction, QIcon, QPixmap, QFont, QColor
from setting import Setting
import os



#making a window class for the notebook app
class NoteBook(QMainWindow):
    def __init__(self, app):
        super().__init__()  #poperly initializing the parent class
        self.app = app
        
        #initializing few variable for future use in the code 
        self.savecount = 0 
        self.filename = ""
        self.undocount = 0

        self.setWindowTitle("NoteBook") #title of the window
        self.setGeometry(350, 150, 800, 600) #seting the aspect ratio of the wndow 
        self.setMinimumHeight(200)
        self.setMinimumWidth(300)
        file_path = os.path.join("images", "NoteBook.png")
        icon = QPixmap(file_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setWindowIcon(icon)
        



        # setting up icon path variable for seemless icon display after connvertion to exectuable
        open_icon_path = file_path = os.path.join("images", "Open_icon.png")

        #setting up menu bar
        menu_bar = self.menuBar()


        #making neccassry menus for the menu bar
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        setting_menu = menu_bar.addMenu("Settings")
        help_menu = menu_bar.addMenu("Help")



        # making necessary action for this menu 
        open_action = QAction(QIcon(open_icon_path), 'Open', self)
        save_action = QAction(QIcon('images/Save_icon.png'), "Save", self)
        save_as_action = QAction(QIcon('images/Save_as_icon.png'), 'Save as', self)
        exit_action = QAction(QIcon('images/Exit_icon.png'), 'Exit', self)
        self.auto_save_action = QAction('Auto Save', self)
        self.auto_save_action.setCheckable(True)


        # adding the action to the file menu 
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(exit_action)
        file_menu.addAction(self.auto_save_action)



        # assigning the fuctionality to these actions 
        exit_action.triggered.connect(self.exit_function)
        open_action.triggered.connect(self.open_file)
        save_as_action.triggered.connect(self.save_file_as)
        save_action.triggered.connect(self.save_file)
        self.auto_save_action.triggered.connect(self.auto_save)



        # making necessary buttons to add to the edit menu
        copy_button = QAction(QIcon('images/Copy_icon.png'), 'Copy', self)
        paste_button = QAction(QIcon("images/Paste_icon.png"), "Paste", self)
        cut_button = QAction(QIcon('images/Cut_icon.png'), 'Cut', self)
        undo_button = QAction(QIcon('images/Undo_icon.png'), "Undo", self)
        redo_button = QAction(QIcon('images/Redo_icon.png'), "Redo", self)



        #adding funtionality to these buttons
        copy_button.triggered.connect(self.copy_text)
        paste_button.triggered.connect(self.paste_text)
        cut_button.triggered.connect(self.cut_text)
        undo_button.triggered.connect(self.undo_text)
        redo_button.triggered.connect(self.redo_text)



        #adding actions to the edit menu 
        edit_menu.addAction(copy_button)
        edit_menu.addAction(paste_button)
        edit_menu.addAction(cut_button)
        edit_menu.addAction(undo_button)
        edit_menu.addAction(redo_button)
        

        # making actions for the setting menu 
        Open_setting_action = QAction("Open Setting", self)


        #adding functionality to these actions
        Open_setting_action.triggered.connect(self.open_setting)

        #adding these actions to setting menu 
        setting_menu.addAction(Open_setting_action)


        # making a toolbar 
        toolbar = QToolBar("tool_bar", self)
        


        # Now adding actions to the toolbar (these action are common along with the menu bar actions)
        toolbar.addAction(copy_button)
        toolbar.addAction(paste_button)
        toolbar.addAction(cut_button)
        toolbar.addAction(undo_button)
        toolbar.addAction(redo_button)
        toolbar.addAction(save_action) 



        #adding this toolbar to the main window
        self.addToolBar(toolbar)



        #making a text space
        self.text_area = QTextEdit(self)
        self.text_area.setTextColor(QColor(50, 100, 250))
        
        # Set the font to Arial with a size of 12
        font = QFont("Consolas", 11)

        # use this font in the text_area
        self.text_area.setFont(font)

        #adding the text area to the window 
        self.setCentralWidget(self.text_area)


        #making a status bar 
        self.status_bar = QStatusBar(self)

        #adding the status bar
        self.setStatusBar(self.status_bar)

        #adding status tip to all the actions
        open_action.setStatusTip("open already existing file")
        save_action.setStatusTip("Save the document")
        save_as_action.setStatusTip("Save the document to your desired format")
        exit_action.setStatusTip("Quit the App")
        copy_button.setStatusTip("Copy the selected text")
        paste_button.setStatusTip("Paste the text from the clipboard")
        cut_button.setStatusTip("Cut the selected text")
        undo_button.setStatusTip("Undo to the last action")
        redo_button.setStatusTip("Redo the last undo")

        #auto saving 
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self.auto_save) 
        self.timer.start(10000)

        

    # making necessary attributes to add to the actions

    def exit_function(self):
        self.app.quit()

    def copy_text(self):
        self.text_area.copy()

    def paste_text(self):
        self.text_area.paste()

    def cut_text(self):
        self.text_area.cut()

    def undo_text(self):
        self.text_area.undo()
        self.undocount += 1

    def redo_text(self):
        if self.undocount > 0:
            self.text_area.redo()
            self.undocount -= 1
        
        else :
            message_box = QMessageBox.information(self, 
                                    'Redo not Available', 
                                    "You cannot do redo right now, You first have to do undo to perform redo", 
                                    QMessageBox.Discard)
            

        
    def open_file(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open file', "C:", "Text FIle(*.txt *.docx)" )
        if self.filename:
            with open(self.filename[0], "r")as file:
                data = file.read()
                self.text_area.setText(data)
    
    def save_file_as(self):
        self.savecount += 1
        self.filename = QFileDialog.getSaveFileName(self, 'Save file', "c:/untitled.txt", "Text File(*.txt *.docx)")
        if self.filename:
            self.save_function()

    def save_file(self):
        if self.savecount < 1 and self.filename == "":
            self.save_file_as()
        elif self.filename != "":
            self.save_function()

    def auto_save(self):
        if self.auto_save_action.isChecked() and len(self.filename) > 0:
            self.save_file()
            
                   
    def open_setting(self):
        self.setting_window = Setting()
        self.setting_window.exec()


    def save_function(self):
        with open(self.filename[0], "w")as file:
                data = self.text_area.toPlainText()
                file.write(data)
                self.status_bar.showMessage("File saved", 1500)
