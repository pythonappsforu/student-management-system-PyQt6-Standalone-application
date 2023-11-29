from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QGridLayout,\
     QLineEdit,QPushButton
import sys
import os
from datetime import datetime

os.environ['QT_FATAL_WARNINGS']='1'
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']=r'E:\python\Python Mega Course Learn Python in 60 Days, Build 20 Apps\Student-Managemnet-System-Pyqt6\venv\Lib\site-packages\PyQt6\Qt6\plugins\platforms'


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()
        # create widgets
        name_label = QLabel('Name:')
        self.name_line_edit = QLineEdit()

        DOB_label = QLabel('Date of Birth DD/MM/YYYY:')
        self.DOB_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # add widgets to grid
        grid.addWidget(name_label,0,0)
        grid.addWidget(self.name_line_edit,0,1)
        grid.addWidget(DOB_label,1,0)
        grid.addWidget(self.DOB_line_edit,1,1)
        grid.addWidget(calculate_button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)

        self.setLayout(grid)

    def calculate_age(self):
        curent_year = datetime.now().year
        date_of_birh = self.DOB_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birh,"%d/%m/%Y").year
        age = curent_year - year_of_birth
        print(age)
        self.output_label.setText(f"Age of {self.name_line_edit.text()} is {age}")




app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
