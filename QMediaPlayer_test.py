from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer # is that all I need to import??
from PyQt5.QtGui import QFont, QIcon, QPixmap
import sys

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.move(100,100)
        self.setWindowTitle('Media Player')

# I don't know how to write a code for the mediaplayer :-/
# The one below doesn't work and is only a guess, since I didn't find a source on the net that explains...
# ...how to code it for Python but only for C++

        self.mediaplayer = QMediaPlayer(self)
        self.mediaplayer.setMedia(QMediaContent(QUrl("vid/dhmis.mp4")))
        self.mediaplayer.setVolume(50)
        self.mediaplayer.play()
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mediaplay = MainWindow()
    sys.exit(app.exec_())
