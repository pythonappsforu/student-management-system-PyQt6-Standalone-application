from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QGridLayout,\
     QLineEdit,QPushButton,QComboBox,QMessageBox,QMainWindow,QTableWidget,QTableWidgetItem,\
      QVBoxLayout,QDialog,QToolBar,QStatusBar
from PyQt6.QtGui import QAction,QIcon
import sqlite3
import faulthandler
import sys
import os

# for debugging purpose
faulthandler.enable()
os.environ['QT_DEBUG_PLUGINS'] = '1'
os.environ['QT_FATAL_WARNINGS']='1'

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']=r'E:\python\Python Mega Course Learn Python in 60 Days, Build 20 Apps\Student-Managemnet-System-Pyqt6\venv\Lib\site-packages\PyQt6\Qt6\plugins\platforms'



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800,600)

        fileMenuItem = self.menuBar().addMenu("&File")
        helpMenuItem = self.menuBar().addMenu("&Help")
        editMenuItem = self.menuBar().addMenu("&Edit")

        add_student_action = QAction(QIcon("icons/add.png"),"Add Student",self)
        add_student_action.triggered.connect(self.insert)
        fileMenuItem.addAction(add_student_action)

        about_help_action = QAction("About",self)
        helpMenuItem.addAction(about_help_action)

        search_action = QAction(QIcon("icons/search.png"),"Search",self)
        search_action.triggered.connect(self.search)
        editMenuItem.addAction(search_action)



        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id','Name','Course','Mobile'))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        #Create toolbar and add toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Add status bar
        self.statusbar=QStatusBar()
        self.setStatusBar(self.statusbar)

        # Detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)
        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        #for resetting table rows
        self.table.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.table.insertRow(row_num)
            for column_num,col_data in enumerate(row_data):

                self.table.setItem(row_num,column_num,QTableWidgetItem(str(col_data)))

        connection.close()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        layout = QVBoxLayout()

        #Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name =QComboBox()
        courses = ['Maths','Physics','Astronomy','Data Science']
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add mobile num widget
        self.mobile_num = QLineEdit()
        self.mobile_num.setPlaceholderText("Mobile num")
        layout.addWidget(self.mobile_num)

        #Add a submit button
        button = QPushButton("Register")
        layout.addWidget(button)
        button.clicked.connect(self.add_student)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_num.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students(name,course,mobile) VALUES (?,?,?)",
                       (name,course,mobile))
        connection.commit()
        cursor.close()
        connection.close()
        mainwindow.load_data()

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add a submit button
        button = QPushButton("Search")
        layout.addWidget(button)
        button.clicked.connect(self.search)

        self.setLayout(layout)
    def search(self):
        name = self.student_name.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name=?",(name,))
        rows= list(result)
        print(rows)
        items = mainwindow.table.findItems(name,Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            mainwindow.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()



app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.load_data()
mainwindow.show()
sys.exit(app.exec())