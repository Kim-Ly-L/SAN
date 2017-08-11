"""
A slightly more interesting example of user interaction.

A window is created with a LCD display, slider, dropdown menu, button and some labels.
The slider can be used to change the x position of the window, which is displayed on
the LCD display. Different ranges for the slider can be chosen.

"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class MyWeight(QWidget):
    def __init__(self):
        super(MyWeight, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(300)  #U SHALL NOT RESIZE ME!!!!!!
        self.setFixedHeight(200) #RHHHHHAAAAWWWW
        self.move(20,20)
        self.setWindowTitle('Scales')
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
        	background-color: qlineargradient(x1: 0 ,y1: 0 ,x2: 1 ,y2: 1,
        						stop: 0 White, stop: 0.7 #558ed2);

         }
         """)
        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(0, 0, 300, 80) #x = Breite
        label_weight = QLabel(self.lcd) # embedded into lcd
        label_weight.setText("Weight in kg")
        label_weight.setGeometry(10, 10, 200, 50)
        label_weight.setObjectName("weight")
        label_weight.setStyleSheet("""
         QLabel#weight {
            font-family: Helvetica;
            font-size: 15px;
        	color: white;
            font-weight: bold;
         }
         """)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(30, 50)
        self.slider.setFixedWidth(290)
        self.slider.move(5, 80)
        self.slider.valueChanged.connect(self.sliderChanged)
        label_range = QLabel(self)
        label_range.setText("Weight Category: ")
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(["30-50", "50-100", "100-200"])
        self.dropdown.currentIndexChanged.connect(self.rangeChanged)
        label_range.move(60, 140)
        self.dropdown.move(150, 135)
        self.button = QPushButton(self)
        self.button.setText("Submit")
        self.button.clicked.connect(self.submit)
        self.button.move(150, 160)
        self.show()

    def submit(self):
        pass

    def sliderChanged(self):
        newval = self.slider.value()
        self.lcd.display(newval)

    def rangeChanged(self):
        item = self.dropdown.currentText()
        if item == "30-50":
            self.slider.setRange(30, 50)
        elif item == "50-100":
            self.slider.setRange(50, 100)
        elif item == "100-200":
            self.slider.setRange(100, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weighty = MyWeight()
    sys.exit(app.exec_())
