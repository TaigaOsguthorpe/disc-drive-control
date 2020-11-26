from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtCore import QThread
#from gui.no_skin import Ui_MainWindow
from gui.skined import Ui_MainWindow
import ctypes
import platform
import os
# THREADING TEST
import time



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.platform = platform.system()

        self.ui.pushButton.clicked.connect(self.open_drive)
        self.ui.pushButton_2.clicked.connect(self.close_drive)

        self.ui.actionAbout_QT.triggered.connect(self.about_qt)

        # Threading test
        self.custom_thread = CustomThread()
        self.custom_thread.start()



    def closeEvent(self, event):
        self.custom_thread.stop()
        #app.quit()
        #event.accept()


    def open_drive(self):
        if self.platform == "Windows":
            ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)

        elif self.platform == "Linux":
            os.system("eject cdrom")

        elif self.platform == "FreeBSD":
            os.system("cdcontrol eject")

        elif self.platform == "NetBSD":
            os.system("eject cd")

        elif self.platform == "Darwin":
            os.system("drutil tray open")

        else:
            return



    def close_drive(self):
        if self.platform == "Windows":
            ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)

        elif self.platform == "Linux":
            os.system("eject -t cdrom")

        elif self.platform == "FreeBSD":
            os.system("cdcontrol close")

        elif self.platform == "NetBSD":
            os.system("eject -t cd")

        elif self.platform == "Darwin":  # macOS
            os.system("drutil tray closed")

        else:
            return



    def about_qt(self):
        QMessageBox.aboutQt(self)



class CustomThread(QThread):
    def run(self):
        while not self.isInterruptionRequested():
            print("Thread is Running")
            time.sleep(1)

    def stop(self):
        print("Thread Stopped")
        self.requestInterruption()
        self.wait()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
