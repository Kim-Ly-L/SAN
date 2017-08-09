from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QGridLayout, QHBoxLayout, QAbstractItemView
from PyQt5.QtWidgets import QComboBox, QSpinBox, QListWidget, QLineEdit, QPlainTextEdit, QPushButton
from PyQt5.QtWidgets import QWidget, QRadioButton, QCheckBox, QGroupBox, QProgressBar, QSlider, QMessageBox
from PyQt5.QtCore import Qt
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        mf_layout = QHBoxLayout()
        mf_layout.addWidget(QMfButton1("Light"))
        mf_layout.addWidget(QMfButton2("Medium"))
        mf_layout.addWidget(QMfButton3("Heavy"))
        menstruationflow = QGroupBox("MENSTRUATION FLOW")
        menstruationflow.setLayout(mf_layout)
        menstruationflow.setMaximumSize(400, 190)

        lifestyle_layout = QHBoxLayout()
        lifestyle_layout.addWidget(QLsButton1("Weight"))
        lifestyle_layout.addWidget(QLsButton2("Sleep"))
        lifestyle_layout.addWidget(QLsButton3("Nutrition"))
        lifestyle_layout.addWidget(QLsButton4("Steps"))
        lsbuttons = QGroupBox("LIFESTYLE")
        lsbuttons.setLayout(lifestyle_layout)
        lsbuttons.setMaximumSize(400, 190)

        ssd_layout = QHBoxLayout()
        ssd_layout.addWidget(QSsdButton1("Didn't have Sex"))
        ssd_layout.addWidget(QSsdButton2("Protected Sex"))
        ssd_layout.addWidget(QSsdButton3("Unprotected Sex"))
        ssd_layout.addWidget(QSsdButton4("High Sex Drive"))
        ssd_layout.addWidget(QSsdButton5("Masturbation"))
        ssdbuttons = QGroupBox("SEX AND SEX DRIVE")
        ssdbuttons.setLayout(ssd_layout)
        ssdbuttons.setMaximumSize(400, 190)

        hay_layout = QHBoxLayout()
        hay_layout.addWidget(QHayButton1("Normal"))
        hay_layout.addWidget(QHayButton2("Happy"))
        hay_layout.addWidget(QHayButton3("Frisky"))
        hay_layout.addWidget(QHayButton4("Mood Swings"))
        hay_layout.addWidget(QHayButton5("Angry"))
        hay_layout.addWidget(QHayButton6("Sad"))
        hay_layout.addWidget(QHayButton7("Panicky"))
        haybuttons = QGroupBox("HOW ARE YOU?")
        haybuttons.setLayout(hay_layout)
        haybuttons.setMaximumSize(400, 190)

        logs_layout = QHBoxLayout()
        logs_layout.addWidget(QLogsButton1("Everything is fine"))
        logs_layout.addWidget(QLogsButton2("Cramps"))
        logs_layout.addWidget(QLogsButton3("Tender Breasts"))
        logs_layout.addWidget(QLogsButton4("Headache"))
        logs_layout.addWidget(QLogsButton5("Backache"))
        logs_layout.addWidget(QLogsButton6("Fatigue"))
        logs_layout.addWidget(QLogsButton7("Bloating"))
        logs_layout.addWidget(QLogsButton8("Cravings"))
        logs_layout.addWidget(QLogsButton9("Insomnia"))
        logs_layout.addWidget(QLogsButton7("Constipation"))
        logs_layout.addWidget(QLogsButton7("Diarrhea"))
        logsbuttons = QGroupBox("LOG SYMPTOMS")
        logsbuttons.setLayout(logs_layout)
        logsbuttons.setMaximumSize(400, 190)

        other_layout = QHBoxLayout()
        other_layout.addWidget(QOtButton1("Travel"))
        other_layout.addWidget(QOtButton2("Stress"))
        other_layout.addWidget(QOtButton3("Disease"))
        other_layout.addWidget(QOtButton4("Alcohol"))
        otbuttons = QGroupBox("OTHER")
        otbuttons.setLayout(other_layout)
        otbuttons.setMaximumSize(400, 190)

        #radios_layout = QHBoxLayout()
        #radios_layout.addWidget(QRadioButton("Radio 1"))
        #radios_layout.addWidget(QRadioButton("Radio 2"))
        #radios_layout.addWidget(QRadioButton("Radio 3"))
        #radiobuttons = QGroupBox("Radio Buttons")
        #radiobuttons.setLayout(radios_layout)
        #radiobuttons.setMaximumSize(300, 70)

        c
