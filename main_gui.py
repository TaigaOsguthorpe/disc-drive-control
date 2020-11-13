from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtCore import QFile
#from gui.no_skin import Ui_MainWindow
from gui.skined import Ui_MainWindow
import ctypes


class MainWindow(QMainWindow):

    def open_drive(self):
        ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)


    def close_drive(self):
        ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)


    def about_qt(self):
        QMessageBox.aboutQt(self)


    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.open_drive)
        self.ui.pushButton_2.clicked.connect(self.close_drive)

        self.ui.actionAbout_QT.triggered.connect(self.about_qt)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
