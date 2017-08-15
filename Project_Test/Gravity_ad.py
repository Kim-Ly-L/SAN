from PyQt5.QtWidgets import QApplication, qApp, QWidget, QLabel
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QIcon, QPixmap
import sys

class GravityWindow(QWidget):
    def __init__(self, xpos, ypos, title):
        super(GravityWindow, self).__init__()
        self.acceleration = 5.0
        self.velocity = 0.0
        self.screenHeight = qApp.desktop().availableGeometry().height() # height of the screen
        self.sound = QSound("sounds/Sosumi.wav")
        self.makeWin(xpos, ypos, title)

    def makeWin(self, xpos, ypos, title):
        self.setGeometry(xpos, ypos, 300, 500)
        self.setWindowTitle(title)
        label = QLabel(self)
        pixmap = QPixmap('img/always.png')
        label.setPixmap(pixmap)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animateFrame)
        self.timer.start(1000 / 12) # 12 frames per second

    # this function gets called 12 times per second
    def animateFrame(self):
        xpos = self.pos().x()
        ypos = self.pos().y() + self.velocity # move the ypos a little bit
        if (ypos + self.height()) > self.screenHeight:
            ypos = self.screenHeight - self.height()
            if abs(self.velocity) <= self.acceleration:  # when the velocity is very small, just set it to 0.0 to keep from infinite bouncing
                self.velocity = 0.0
            else:
                self.sound.play()
                self.velocity *= -1.0 # velocity of movement changes direction
        self.move(xpos, ypos)
        self.velocity += self.acceleration


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
            GravityWindow {
                background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop: 0 #ffffff, stop: 1 #333333);
            }
        """)
    win1 = GravityWindow(30, 10, "Advertisement")
    win1.show()
    sys.exit(app.exec_())
