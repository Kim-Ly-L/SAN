from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

#    def closeEvent(self, event):

#        quit_msg = "Are you sure you want to exit the program? We can really help you."
#        reply = QMessageBox.question(self, 'Message',
#                         quit_msg, QMessageBox.Yes, QMessageBox.No)

#        if reply == QMessageBox.Yes:
#            event.ignore()
#            choice = QMessageBox.critical(self, 'Oh, come on.',
#                                         "Don't leave yet. Stay, this way we can help you.")
#        else:
#            event.ignore()

    def ehwk(self):
        choice = QMessageBox.critical(self, 'It\'s too late', #question, information, warning, critical
                                     "Once Information is brought out, it cannot be returned.")


    def popup1(self):

        choice = QMessageBox.question(self, 'Light', #question, information, warning, critical
                                     "Do you want to log in that your flow is \'light\'?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            self.light.setStyleSheet("""
                QCheckBox#light::indicator {
                	width: 60px;
                	height: 60px;
                }
                QCheckBox#light::indicator:unchecked {
                	image: url(img/mf1_sw.png);
                }
                QCheckBox#light::indicator:unchecked:hover {
                	image: url(img/mf1_sw.png);
                }
                QCheckBox#light::indicator:checked {
                	image: url(img/mf1_sw.png);
                }
            """)
            self.light.clicked.connect(self.ehwk)
        else:
            pass

    def initGUI(self):
        self.setGeometry(10, 30, 530, 700)
        self.setWindowTitle("Flo Period Tracker")
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
        	background-color: qlineargradient(x1: 0 ,y1: 0 ,x2: 1 ,y2: 1,
        						stop: 0 #fff2d1, stop: 0.7 Salmon
        						stop: 1 PapayaWhip);

         }
         """)

# BUTTONS:


        self.light = QCheckBox(self)
        self.light.resize(90, 90)
        self.light.setObjectName("light")
        self.light.setStyleSheet("""
            QCheckBox#light::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#light::indicator:unchecked {
            	image: url(img/mf1.png);
            }
            QCheckBox#light::indicator:unchecked:hover {
            	image: url(img/mf1_h.png);
            }
            QCheckBox#light::indicator:checked {
            	image: url(img/mf1.png);
            }
        """)
        self.light.move(20, 80)

        #if #light clicked 1st time:
        self.light.clicked.connect(self.popup1)
    #    else:
    #        self.light.clicked.connect(self.ehwk)

        self.medium = QCheckBox(self)
        self.medium.resize(90, 90)
        self.medium.setObjectName("medium")
        self.medium.setStyleSheet("""
            QCheckBox#medium::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#medium::indicator:unchecked {
            	image: url(img/mf2.png);
            }
            QCheckBox#medium::indicator:unchecked:hover {
            	image: url(img/mf2_h.png);
            }
            QCheckBox#medium::indicator:checked {
            	image: url(img/mf2_sw.png);
            }
        """)
        self.medium.move(90, 80)

        self.heavy = QCheckBox(self)
        self.heavy.resize(90, 90)
        self.heavy.setObjectName("heavy")
        self.heavy.setStyleSheet("""
            QCheckBox#heavy::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#heavy::indicator:unchecked {
            	image: url(img/mf3.png);
            }
            QCheckBox#heavy::indicator:unchecked:hover {
            	image: url(img/mf3_h.png);
            }
            QCheckBox#heavy::indicator:checked {
            	image: url(img/mf3_sw.png);
            }
        """)
        self.heavy.move(160, 80)

        self.weight = QCheckBox(self)
        self.weight.resize(90, 90)
        self.weight.setObjectName("weight")
        self.weight.setStyleSheet("""
            QCheckBox#weight::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#weight::indicator:unchecked {
            	image: url(img/weight.png);
            }
            QCheckBox#weight::indicator:unchecked:hover {
            	image: url(img/weight_h.png);
            }
            QCheckBox#weight::indicator:checked {
            	image: url(img/weight_sw.png);
            }
        """)
        self.weight.move(20, 180)

        self.sleep = QCheckBox(self)
        self.sleep.resize(90, 90)
        self.sleep.setObjectName("sleep")
        self.sleep.setStyleSheet("""
            QCheckBox#sleep::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#sleep::indicator:unchecked {
            	image: url(img/sleep.png);
            }
            QCheckBox#sleep::indicator:unchecked:hover {
            	image: url(img/sleep_h.png);
            }
            QCheckBox#sleep::indicator:checked {
            	image: url(img/sleep_sw.png);
            }
        """)
        self.sleep.move(90, 180)

        self.nutrition = QCheckBox(self)
        self.nutrition.resize(90, 90)
        self.nutrition.setObjectName("nutrition")
        self.nutrition.setStyleSheet("""
            QCheckBox#nutrition::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#nutrition::indicator:unchecked {
            	image: url(img/nutrition.png);
            }
            QCheckBox#nutrition::indicator:unchecked:hover {
            	image: url(img/nutrition_h.png);
            }
            QCheckBox#nutrition::indicator:checked {
            	image: url(img/nutrition_sw.png);
            }
        """)
        self.nutrition.move(160, 180)

        self.steps = QCheckBox(self)
        self.steps.resize(90, 90)
        self.steps.setObjectName("steps")
        self.steps.setStyleSheet("""
            QCheckBox#steps::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#steps::indicator:unchecked {
            	image: url(img/steps.png);
            }
            QCheckBox#steps::indicator:unchecked:hover {
            	image: url(img/steps_h.png);
            }
            QCheckBox#steps::indicator:checked {
            	image: url(img/steps_sw.png);
            }
        """)
        self.steps.move(230, 180)

        self.nosex = QCheckBox(self)
        self.nosex.resize(90, 90)
        self.nosex.setObjectName("nosex")
        self.nosex.setStyleSheet("""
            QCheckBox#nosex::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#nosex::indicator:unchecked {
            	image: url(img/no_sex.png);
            }
            QCheckBox#nosex::indicator:unchecked:hover {
            	image: url(img/no_sex_h.png);
            }
            QCheckBox#nosex::indicator:checked {
            	image: url(img/no_sex_sw.png);
            }
        """)
        self.nosex.move(20, 280)

        self.protected = QCheckBox(self)
        self.protected.resize(90, 90)
        self.protected.setObjectName("protected")
        self.protected.setStyleSheet("""
            QCheckBox#protected::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#protected::indicator:unchecked {
            	image: url(img/protected_sex.png);
            }
            QCheckBox#protected::indicator:unchecked:hover {
            	image: url(img/protected_sex_h.png);
            }
            QCheckBox#protected::indicator:checked {
            	image: url(img/protected_sex_sw.png);
            }
        """)
        self.protected.move(90, 280)

        self.unprotected = QCheckBox(self)
        self.unprotected.resize(90, 90)
        self.unprotected.setObjectName("unprotected")
        self.unprotected.setStyleSheet("""
            QCheckBox#unprotected::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#unprotected::indicator:unchecked {
            	image: url(img/unprotected_sex.png);
            }
            QCheckBox#unprotected::indicator:unchecked:hover {
            	image: url(img/unprotected_sex_h.png);
            }
            QCheckBox#unprotected::indicator:checked {
            	image: url(img/unprotected_sex_sw.png);
            }
        """)
        self.unprotected.move(160, 280)

        self.high = QCheckBox(self)
        self.high.resize(90, 90)
        self.high.setObjectName("high")
        self.high.setStyleSheet("""
            QCheckBox#high::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#high::indicator:unchecked {
            	image: url(img/high_sex.png);
            }
            QCheckBox#high::indicator:unchecked:hover {
            	image: url(img/high_sex_h.png);
            }
            QCheckBox#high::indicator:checked {
            	image: url(img/high_sex_sw.png);
            }
        """)
        self.high.move(230, 280)

        self.unprotected = QCheckBox(self)
        self.unprotected.resize(90, 90)
        self.unprotected.setObjectName("unprotected")
        self.unprotected.setStyleSheet("""
            QCheckBox#unprotected::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#unprotected::indicator:unchecked {
            	image: url(img/unprotected_sex.png);
            }
            QCheckBox#unprotected::indicator:unchecked:hover {
            	image: url(img/unprotected_sex_h.png);
            }
            QCheckBox#unprotected::indicator:checked {
            	image: url(img/unprotected_sex_sw.png);
            }
        """)
        self.unprotected.move(160, 280)

        self.masturbation = QCheckBox(self)
        self.masturbation.resize(90, 90)
        self.masturbation.setObjectName("masturbation")
        self.masturbation.setStyleSheet("""
            QCheckBox#masturbation::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#masturbation::indicator:unchecked {
            	image: url(img/Masturbation.png);
            }
            QCheckBox#masturbation::indicator:unchecked:hover {
            	image: url(img/Masturbation_h.png);
            }
            QCheckBox#masturbation::indicator:checked {
            	image: url(img/Masturbation_sw.png);
            }
        """)
        self.masturbation.move(300, 280)

        self.normal = QCheckBox(self)
        self.normal.resize(90, 90)
        self.normal.setObjectName("normal")
        self.normal.setStyleSheet("""
            QCheckBox#normal::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#normal::indicator:unchecked {
            	image: url(img/Normal.png);
            }
            QCheckBox#normal::indicator:unchecked:hover {
            	image: url(img/Normal_h.png);
            }
            QCheckBox#normal::indicator:checked {
            	image: url(img/Normal_sw.png);
            }
        """)
        self.normal.move(20, 380)

        self.happy = QCheckBox(self)
        self.happy.resize(90, 90)
        self.happy.setObjectName("happy")
        self.happy.setStyleSheet("""
            QCheckBox#happy::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#happy::indicator:unchecked {
            	image: url(img/Happy.png);
            }
            QCheckBox#happy::indicator:unchecked:hover {
            	image: url(img/Happy_h.png);
            }
            QCheckBox#happy::indicator:checked {
            	image: url(img/Happy_sw.png);
            }
        """)
        self.happy.move(90, 380)

        self.frisky = QCheckBox(self)
        self.frisky.resize(90, 90)
        self.frisky.setObjectName("frisky")
        self.frisky.setStyleSheet("""
            QCheckBox#frisky::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#frisky::indicator:unchecked {
            	image: url(img/Frisky.png);
            }
            QCheckBox#frisky::indicator:unchecked:hover {
            	image: url(img/Frisky_h.png);
            }
            QCheckBox#frisky::indicator:checked {
            	image: url(img/Frisky_sw.png);
            }
        """)
        self.frisky.move(160, 380)

        self.moodswings = QCheckBox(self)
        self.moodswings.resize(90, 90)
        self.moodswings.setObjectName("moodswings")
        self.moodswings.setStyleSheet("""
            QCheckBox#moodswings::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#moodswings::indicator:unchecked {
            	image: url(img/Mood_swings.png);
            }
            QCheckBox#moodswings::indicator:unchecked:hover {
            	image: url(img/Mood_swings_h.png);
            }
            QCheckBox#moodswings::indicator:checked {
            	image: url(img/Mood_swings_sw.png);
            }
        """)
        self.moodswings.move(230, 380)

        self.angry = QCheckBox(self)
        self.angry.resize(90, 90)
        self.angry.setObjectName("angry")
        self.angry.setStyleSheet("""
            QCheckBox#angry::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#angry::indicator:unchecked {
            	image: url(img/Angry.png);
            }
            QCheckBox#angry::indicator:unchecked:hover {
            	image: url(img/Angry_h.png);
            }
            QCheckBox#angry::indicator:checked {
            	image: url(img/Angry_sw.png);
            }
        """)
        self.angry.move(300, 380)

        self.sad = QCheckBox(self)
        self.sad.resize(90, 90)
        self.sad.setObjectName("sad")
        self.sad.setStyleSheet("""
            QCheckBox#sad::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#sad::indicator:unchecked {
            	image: url(img/Sad.png);
            }
            QCheckBox#sad::indicator:unchecked:hover {
            	image: url(img/Sad_h.png);
            }
            QCheckBox#sad::indicator:checked {
            	image: url(img/Sad_sw.png);
            }
        """)
        self.sad.move(370, 380)

        self.fine = QCheckBox(self)
        self.fine.resize(90, 90)
        self.fine.setObjectName("fine")
        self.fine.setStyleSheet("""
            QCheckBox#fine::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#fine::indicator:unchecked {
            	image: url(img/fine.png);
            }
            QCheckBox#fine::indicator:unchecked:hover {
            	image: url(img/fine_h.png);
            }
            QCheckBox#fine::indicator:checked {
            	image: url(img/fine_sw.png);
            }
        """)
        self.fine.move(20, 480)

        self.cramps = QCheckBox(self)
        self.cramps.resize(90, 90)
        self.cramps.setObjectName("cramps")
        self.cramps.setStyleSheet("""
            QCheckBox#cramps::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#cramps::indicator:unchecked {
            	image: url(img/cramps.png);
            }
            QCheckBox#cramps::indicator:unchecked:hover {
            	image: url(img/cramps_h.png);
            }
            QCheckBox#cramps::indicator:checked {
            	image: url(img/cramps_sw.png);
            }
        """)
        self.cramps.move(90, 480)

        self.tender = QCheckBox(self)
        self.tender.resize(90, 90)
        self.tender.setObjectName("tender")
        self.tender.setStyleSheet("""
            QCheckBox#tender::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#tender::indicator:unchecked {
            	image: url(img/tender.png);
            }
            QCheckBox#tender::indicator:unchecked:hover {
            	image: url(img/tender_h.png);
            }
            QCheckBox#tender::indicator:checked {
            	image: url(img/tender_sw.png);
            }
        """)
        self.tender.move(160, 480)

        self.headache = QCheckBox(self)
        self.headache.resize(90, 90)
        self.headache.setObjectName("headache")
        self.headache.setStyleSheet("""
            QCheckBox#headache::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#headache::indicator:unchecked {
            	image: url(img/Headache.png);
            }
            QCheckBox#headache::indicator:unchecked:hover {
            	image: url(img/Headache_h.png);
            }
            QCheckBox#headache::indicator:checked {
            	image: url(img/Headache_sw.png);
            }
        """)
        self.headache.move(230, 480)

        self.fatigue = QCheckBox(self)
        self.fatigue.resize(90, 90)
        self.fatigue.setObjectName("fatigue")
        self.fatigue.setStyleSheet("""
            QCheckBox#fatigue::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#fatigue::indicator:unchecked {
            	image: url(img/Fatique.png);
            }
            QCheckBox#fatigue::indicator:unchecked:hover {
            	image: url(img/Fatique_h.png);
            }
            QCheckBox#fatigue::indicator:checked {
            	image: url(img/Fatique_sw.png);
            }
        """)
        self.fatigue.move(300, 480)

        self.bloating = QCheckBox(self)
        self.bloating.resize(90, 90)
        self.bloating.setObjectName("bloating")
        self.bloating.setStyleSheet("""
            QCheckBox#bloating::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#bloating::indicator:unchecked {
            	image: url(img/Bloating.png);
            }
            QCheckBox#bloating::indicator:unchecked:hover {
            	image: url(img/Bloating_h.png);
            }
            QCheckBox#bloating::indicator:checked {
            	image: url(img/Bloating_sw.png);
            }
        """)
        self.bloating.move(370, 480)

        self.cravings = QCheckBox(self)
        self.cravings.resize(90, 90)
        self.cravings.setObjectName("cravings")
        self.cravings.setStyleSheet("""
            QCheckBox#cravings::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#cravings::indicator:unchecked {
            	image: url(img/Cravings.png);
            }
            QCheckBox#cravings::indicator:unchecked:hover {
            	image: url(img/Cravings_h.png);
            }
            QCheckBox#cravings::indicator:checked {
            	image: url(img/Cravings_sw.png);
            }
        """)
        self.cravings.move(440, 480)

        self.travel = QCheckBox(self)
        self.travel.resize(90, 90)
        self.travel.setObjectName("travel")
        self.travel.setStyleSheet("""
            QCheckBox#travel::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#travel::indicator:unchecked {
            	image: url(img/Travel.png);
            }
            QCheckBox#travel::indicator:unchecked:hover {
            	image: url(img/Travel_h.png);
            }
            QCheckBox#travel::indicator:checked {
            	image: url(img/Travel_sw.png);
            }
        """)
        self.travel.move(20, 580)

        self.stress = QCheckBox(self)
        self.stress.resize(90, 90)
        self.stress.setObjectName("stress")
        self.stress.setStyleSheet("""
            QCheckBox#stress::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#stress::indicator:unchecked {
            	image: url(img/Stress.png);
            }
            QCheckBox#stress::indicator:unchecked:hover {
            	image: url(img/Stress_h.png);
            }
            QCheckBox#stress::indicator:checked {
            	image: url(img/Stress_sw.png);
            }
        """)
        self.stress.move(90, 580)

        self.alcohol = QCheckBox(self)
        self.alcohol.resize(90, 90)
        self.alcohol.setObjectName("alcohol")
        self.alcohol.setStyleSheet("""
            QCheckBox#alcohol::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#alcohol::indicator:unchecked {
            	image: url(img/alcohol.png);
            }
            QCheckBox#alcohol::indicator:unchecked:hover {
            	image: url(img/alcohol_h.png);
            }
            QCheckBox#alcohol::indicator:checked {
            	image: url(img/alcohol_sw.png);
            }
        """)
        self.alcohol.move(160, 580)

        self.disease = QCheckBox(self)
        self.disease.resize(90, 90)
        self.disease.setObjectName("disease")
        self.disease.setStyleSheet("""
            QCheckBox#disease::indicator {
            	width: 60px;
            	height: 60px;
            }
            QCheckBox#disease::indicator:unchecked {
            	image: url(img/disease.png);
            }
            QCheckBox#disease::indicator:unchecked:hover {
            	image: url(img/disease_h.png);
            }
            QCheckBox#disease::indicator:checked {
            	image: url(img/disease_sw.png);
            }
        """)
        self.disease.move(230, 580)

# LABELS:

        mf_label = QLabel(self)
        mf_label.setText("MENSTRUATION FLOW")
        mf_label.setGeometry(20, 72, 200, 15)
        mf_label.setObjectName("mf")
        mf_label.setStyleSheet("""
         QLabel#mf {
            font-family: Helvetica;
            font-size: 12px;
        	color: white;
            font-weight: bold;

         }
         """)

        lifest_label = QLabel(self)
        lifest_label.setText("LIFESTYLE ADVICE")
        lifest_label.setGeometry(20, 172, 200, 15)
        lifest_label.setObjectName("lifestyle")
        lifest_label.setStyleSheet("""
         QLabel#lifestyle {
            font-family: Helvetica;
            font-size: 12px;
        	color: white;
            font-weight: bold;
         }
         """)

        sex_label = QLabel(self)
        sex_label.setText("SEX AND SEX DRIVE")
        sex_label.setGeometry(20, 272, 200, 15)
        sex_label.setObjectName("sex")
        sex_label.setStyleSheet("""
         QLabel#sex {
            font-family: Helvetica;
            font-size: 12px;
        	color: white;
            font-weight: bold;
         }
         """)

        hay_label = QLabel(self)
        hay_label.setText("HOW ARE YOU?")
        hay_label.setGeometry(20, 372, 200, 15)
        hay_label.setObjectName("hay")
        hay_label.setStyleSheet("""
         QLabel#hay {
            font-family: Helvetica;
            font-size: 12px;
        	color: white;
            font-weight: bold;
         }
         """)

        log_label = QLabel(self)
        log_label.setText("LOG SYMPTOMS")
        log_label.setGeometry(20, 472, 200, 15)
        log_label.setObjectName("log")
        log_label.setStyleSheet("""
         QLabel#log {
            font-family: Helvetica;
            font-size: 12px;
        	color: white;
            font-weight: bold;
         }
         """)

        ot_label = QLabel(self)
        ot_label.setText("OTHERS")
        ot_label.setGeometry(20, 572, 200, 15)
        ot_label.setObjectName("ot")
        ot_label.setStyleSheet("""
         QLabel#ot {
            font-family: Helvetica;
            font-size: 12px;
        	color: white;
            font-weight: bold;
         }
         """)

        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
