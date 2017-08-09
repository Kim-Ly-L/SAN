from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(QCheckBox("Light"))

#        QCheckBox("Light").setObjectName("light")
#        QCheckBox("Light").setStyleSheet("""
#            QCheckBox#light::indicator {
#            	width: 50px;
#            	height: 50px;
#            }
#            QCheckBox#light::indicator:unchecked {
#            	image: url(img/mf1.png);
#            }
#            QCheckBox#light::indicator:unchecked:hover {
#            	image: url(img/mf1_h.png);
#            }
#            QCheckBox#light::indicator:checked {
#            	image: url(img/mf1_sw.png);
#            }
#        """)
        checkbox_layout.addWidget(QCheckBox("Medium"))
        checkbox_layout.addWidget(QCheckBox("heavy"))
        checkboxes = QGroupBox("MENSTRUAL FLOW")
        checkboxes.setLayout(checkbox_layout)
        checkboxes.setMaximumSize(350, 70)


        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(QCheckBox("Weight"))
        checkbox_layout.addWidget(QCheckBox("Sleep"))
        checkbox_layout.addWidget(QCheckBox("Nutrition"))
        checkbox_layout.addWidget(QCheckBox("Steps"))
        checkboxes1 = QGroupBox("LIFESTYLE")
        checkboxes1.setLayout(checkbox_layout)
        checkboxes1.setMaximumSize(465, 70)

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(QCheckBox("No Sex"))
        checkbox_layout.addWidget(QCheckBox("Protected Sex"))
        checkbox_layout.addWidget(QCheckBox("Unprotected Sex"))
        checkbox_layout.addWidget(QCheckBox("High Sex Drive"))
        checkbox_layout.addWidget(QCheckBox("Masturbation"))
        checkboxes2 = QGroupBox("SEX AND SEX DRIVE")
        checkboxes2.setLayout(checkbox_layout)
        checkboxes2.setMaximumSize(585, 70)

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(QCheckBox("Normal"))
        checkbox_layout.addWidget(QCheckBox("Happy"))
        checkbox_layout.addWidget(QCheckBox("Frisky"))
        checkbox_layout.addWidget(QCheckBox("Mood Swings"))
        checkbox_layout.addWidget(QCheckBox("Angry"))
        checkbox_layout.addWidget(QCheckBox("Sad"))
        checkboxes3 = QGroupBox("HOW ARE YOU?")
        checkboxes3.setLayout(checkbox_layout)
        checkboxes3.setMaximumSize(700, 70)

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(QCheckBox("Everything's fine"))
        checkbox_layout.addWidget(QCheckBox("Cramps"))
        checkbox_layout.addWidget(QCheckBox("Tender Breasts"))
        checkbox_layout.addWidget(QCheckBox("Headache"))
        checkbox_layout.addWidget(QCheckBox("Backache"))
        checkbox_layout.addWidget(QCheckBox("Fatigue"))
        checkboxes4 = QGroupBox("LOG SYMPTOMS")
        checkboxes4.setLayout(checkbox_layout)
        checkboxes4.setMaximumSize(700, 70)

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(QCheckBox("Travel"))
        checkbox_layout.addWidget(QCheckBox("Stress"))
        checkbox_layout.addWidget(QCheckBox("Disease"))
        checkbox_layout.addWidget(QCheckBox("Alcohol"))
        checkboxes5 = QGroupBox("OTHERS")
        checkboxes5.setLayout(checkbox_layout)
        checkboxes5.setMaximumSize(465, 70)

        grid = QGridLayout()
        grid.addWidget(checkboxes,      0, 0, 1, 6) # Y row, X column, rowspan, columnspan
        grid.addWidget(checkboxes1,     1, 0, 1, 6) # span 1 row, 2 columns
        grid.addWidget(checkboxes2,     2, 0, 1, 6)
        grid.addWidget(checkboxes3,     3, 0, 1, 6)
        grid.addWidget(checkboxes4,     4, 0, 1, 6)
        grid.addWidget(checkboxes5,     5, 0, 1, 6)

        mainwidget = QWidget()
        mainwidget.setLayout(grid)
        mainwidget.setObjectName("main")
        self.setCentralWidget(mainwidget)
        self.setWindowTitle("Flo Period Tracker")
        self.setGeometry(20,40,800,600)
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
             background-color: floralwhite

         }
         """)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
