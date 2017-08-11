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

class MySleep(QWidget):
    def __init__(self):
        super(MySleep, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(300)  #U SHALL NOT RESIZE ME!!!!!!
        self.setFixedHeight(200) #RHHHHHAAAAWWWW
        self.move(20,20)
        self.setWindowTitle('SLEEP')
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
        	background-color: qlineargradient(x1: 0 ,y1: 0 ,x2: 1 ,y2: 1,
        						stop: 0 White, stop: 0.7 #558ed2);

         }
         """)
        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(0, 0, 300, 80) #x = Breite
        label_hours = QLabel(self.lcd) # embedded into lcd
        label_hours.setText("Hours last night")
        label_hours.setGeometry(10, 10, 200, 50)
        label_hours.setObjectName("hours")
        label_hours.setStyleSheet("""
         QLabel#hours {
            font-family: Helvetica;
            font-size: 15px;
        	color: white;
            font-weight: bold;
         }
         """)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 15)
        self.slider.setFixedWidth(290)
        self.slider.move(5, 80)
        self.slider.valueChanged.connect(self.sliderChanged)
        label_range = QLabel(self)
        label_range.setText("Hours per night on average ")
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(["3-5", "6-8", "9-12"])
#        self.dropdown.currentIndexChanged.connect(self.rangeChanged)
        label_range.move(10, 140)
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

#    def rangeChanged(self):
#        item = self.dropdown.currentText()
#        if item == "3-5":
#            self.slider.setRange(3, 5)
#        elif item == "6-8":
#            self.slider.setRange(6, 8)
#        elif item == "9-12":
#            self.slider.setRange(9, 12)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sleepy = MySleep()
    sys.exit(app.exec_())
