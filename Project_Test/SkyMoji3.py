from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QRect
import sys

class SkyMoji3(QWidget):
    def __init__(self, imgpath, parent=None):
        super(SkyMoji3, self).__init__(parent)
        self.currentFrame = 0
        self.setPixmap(QPixmap(imgpath))
        self.startTimer(1000 / 15) # animate at 15 fps

    def setPixmap(self, pix):
        self.pixmap = pix
        self.frameWidth = pix.rect().width()
        self.frameHeight = self.frameWidth # Skype emoticons are perfect squares
        self.numFrames = pix.rect().height() / self.frameHeight # Calculate number of frames in the animation
        self.resize(self.frameWidth, self.frameHeight)

    def paintEvent(self, event):
        qp = QPainter(self)
        ypos = self.frameHeight * self.currentFrame # which part of the image to display
        sourceRect = QRect(0, ypos, self.frameWidth, self.frameHeight)
        qp.drawPixmap(self.rect(), self.pixmap, sourceRect) # copy the part of the image in sourceRect to the canvas, scaling if necessary

    def timerEvent(self, event):
        self.currentFrame += 1
        if self.currentFrame == self.numFrames:
            self.currentFrame = 0 # start the animation back at frame 0
        self.update() # force the widget to redraw itself

if __name__ == '__main__':
    app = QApplication(sys.argv)
    filepath = "img/shake_anim@2x.png"
    mywidget3 = SkyMoji3(filepath)
    mywidget3.setGeometry(50, 50, 200, 200)
    mywidget3.setWindowTitle("Unprotected Sex")
    mywidget3.show()
    sys.exit(app.exec_())
