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

    scales = QWidget(self)

    def initUI(self):
        self.scales.setFixedWidth(300)  #U SHALL NOT RESIZE ME!!!!!!
        self.scales.etFixedHeight(200) #RHHHHHAAAAWWWW
        self.scales.move(20,20)
        self.scales.setWindowTitle('Scales')
        self.scales.setObjectName("main")
        self.scales.setStyleSheet("""
         QWidget#main {
        	background-color: qlineargradient(x1: 0 ,y1: 0 ,x2: 1 ,y2: 1,
        						stop: 0 Bisque, stop: 0.7 Coral);

         }
         """)
        self.scales.lcd = QLCDNumber(self.scales)
        self.scales.lcd.setGeometry(0, 0, 300, 80) #x = Breite
        label_weight = QLabel(self.scales.lcd) # embedded into lcd
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

        self.scales.slider = QSlider(Qt.Horizontal, self.scales)
        self.scales.lider.setRange(30, 50)
        self.scales.slider.setFixedWidth(290)
        self.scales.slider.move(5, 80)
        self.scales.slider.valueChanged.connect(self.scales.sliderChanged)
        label_range = QLabel(self.scales)
        label_range.setText("kg: ")
        self.scales.dropdown = QComboBox(self.scales)
        self.scales.dropdown.addItems(["30-50", "50-100", "100-200"])
        self.scales.dropdown.currentIndexChanged.connect(self.scales.rangeChanged)
        label_range.move(105, 140)
        self.scales.dropdown.move(150, 135)
        self.scales.button = QPushButton(self.scales)
        self.scales.button.setText("Submit")
        self.scales.button.clicked.connect(self.scales.submit)
        self.scales.button.move(150, 160)
        self.scales.show()

    def submit(self):  # OBSERVER PATTERN: 3 Dependencies
        sys.exit()

    def sliderChanged(self):  # OBSERVER PATTERN: 3 Dependencies
        newval = self.scales.slider.value()
        self.scales.lcd.display(newval)

    def rangeChanged(self):
        item = self.scales.dropdown.currentText()
        if item == "30-50":
            self.scales.slider.setRange(30, 50)
        elif item == "50-100":
            self.scales.slider.setRange(50, 100)
        elif item == "100-200":
            self.scales.slider.setRange(100, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWindow()
    sys.exit(app.exec_())
