from PyQt6.QtWidgets import QMessageBox


class Calculators:
    def __init__(self, distance, total_time):
        self.distance = distance

        if "/" in total_time:
            total_time_list = total_time.split("/")
            try:
                total_hours = float(total_time_list[0])
                total_minutes = float(total_time_list[1])
            except ValueError:
                self.show_error_dialog("Please only use numbers and '/'!")
                return
            self.decimal_total_time = total_hours + (total_minutes / 60)
        else:
            try:
                self.total_time = float(total_time)
            except ValueError:
                self.show_error_dialog("Please only use numbers!")
                return

    def show_error_dialog(self, message):
        dialog = QMessageBox()
        dialog.setText(message)
        dialog.setWindowTitle("Value error")
        dialog.exec()

    def calculate_average_speed(self, converted_distance):
        if hasattr(self, "decimal_total_time"):
            average_speed = converted_distance / self.decimal_total_time
        else:
            average_speed = converted_distance / self.total_time

        return average_speed

    def miles_to_kmh(self):
        kilometers = self.distance * 1.609344
        average_speed = self.calculate_average_speed(kilometers)
        return average_speed, "km/h"

    def kilometers_to_kmh(self):
        average_speed = self.calculate_average_speed(self.distance)
        return average_speed, "km/h"

    def miles_to_mph(self):
        average_speed = self.calculate_average_speed(self.distance)
        return average_speed, "mph"

    def kilometers_to_mph(self):
        miles = self.distance * 0.621371
        average_speed = self.calculate_average_speed(miles)

        return average_speed, "mph"