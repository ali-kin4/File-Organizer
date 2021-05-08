from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import os
import tkinter as tk
from tkinter import filedialog
import winsound
import organizer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon("FO.ico"))
        MainWindow.resize(342, 89)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(20, 20, 141, 51))
        self.load.setObjectName("load")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(180, 20, 141, 51))
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)

        self.start.setEnabled(False)
        self.load.clicked.connect(lambda: self.loader())
        self.start.clicked.connect(lambda: self.starter())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Organizer"))
        self.load.setText(_translate("MainWindow", "Load Folder"))
        self.start.setText(_translate("MainWindow", "Start"))

    def loader(self):
        root = tk.Tk()
        root.withdraw()
        direction = filedialog.askdirectory(title = "Select the directory")
        if (not direction):
            print("No direction selected.")
        else:
            os.chdir(direction)
            self.start.setEnabled(True)

    def starter(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        organizer.organize()
        QApplication.restoreOverrideCursor()
        winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
