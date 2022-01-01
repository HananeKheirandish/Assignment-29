from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Color_Picker(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('color_picker.ui', None)
        self.ui.show()

        self.ui.red_slider.valueChanged.connect(self.label_colors)
        self.ui.green_slider.valueChanged.connect(self.label_colors)
        self.ui.blue_slider.valueChanged.connect(self.label_colors)

    def label_colors(self):
        self.Red = self.ui.red_slider.value()
        self.Green = self.ui.green_slider.value()
        self.Blue = self.ui.blue_slider.value()

        self.ui.red_num.setText(str(self.Red))
        self.ui.green_num.setText(str(self.Green))
        self.ui.blue_num.setText(str(self.Blue))

        self.find_color()

    def find_color(self):
        self.ui.color.setText(f'rgb({self.Red}, {self.Green}, {self.Blue})')

        self.ui.color.setStyleSheet(f'background-color:rgb({self.Red}, {self.Green}, {self.Blue}); font: 700 14pt "Segoe UI";')
        
        

app = QApplication()
window = Color_Picker()

app.exec()