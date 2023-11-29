from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QGridLayout,\
     QLineEdit,QPushButton,QComboBox,QMessageBox
import sys
import os

from calculators import Calculators

os.environ['QT_FATAL_WARNINGS']='1'
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']=r'E:\python\Python Mega Course Learn Python in 60 Days, Build 20 Apps\Student-Managemnet-System-Pyqt6\venv\Lib\site-packages\PyQt6\Qt6\plugins\platforms'


class AverageSpeedCalculatorGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        from_distance_label = QLabel("From: ")
        self.from_to_combo_box = QComboBox(self)
        self.from_to_combo_box.addItems(["Metric (km)", "Imperial (miles)"])

        distance_label = QLabel("Distance: ")
        self.distance_label_line_edit = QLineEdit()
        to_distance_label = QLabel("To: ")
        self.to_combo_box = QComboBox(self)
        self.to_combo_box.addItems(["Metric (km)", "Imperial (miles)"])

        time_label = QLabel("Time (hours & minutes H/MM): ")
        self.time_label_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        self.output_label = QLabel("")
        calculate_button.clicked.connect(self.calculate_button_clicked)

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_line_edit, 0, 1)
        grid.addWidget(from_distance_label, 0, 2)
        grid.addWidget(self.from_to_combo_box, 0, 3)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_line_edit, 1, 1)
        grid.addWidget(to_distance_label, 1, 2)
        grid.addWidget(self.to_combo_box, 1, 3)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)

    def calculate_button_clicked(self):
        try:
            distance = float(self.distance_label_line_edit.text())
        except ValueError:
            dialog = QMessageBox(text="Please only use numbers!")
            dialog.setWindowTitle("Value error")
            dialog.exec()
            return

        total_time = self.time_label_line_edit.text()
        to_combo_box = self.to_combo_box.currentText()
        from_combo_box = self.from_to_combo_box.currentText()

        calculators = Calculators(distance=distance, total_time=total_time)

        if from_combo_box == "Metric (km)":
            if to_combo_box == "Metric (km)":
                average_speed, unit = calculators.kilometers_to_kmh()
            elif to_combo_box == "Imperial (miles)":
                average_speed, unit = calculators.kilometers_to_mph()
        elif from_combo_box == "Imperial (miles)":
            if to_combo_box == "Imperial (miles)":
                average_speed, unit = calculators.miles_to_mph()
            elif to_combo_box == "Metric (km)":
                average_speed, unit = calculators.miles_to_kmh()

        self.output_label.setText(
            f"Your average speed was: {round(average_speed, 2)} {unit}"
        )


app = QApplication(sys.argv)
average_speed_calculator = AverageSpeedCalculatorGui()
average_speed_calculator.show()
sys.exit(app.exec())
