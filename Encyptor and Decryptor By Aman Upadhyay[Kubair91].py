# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edv_5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 551, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 110, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 520, 551, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 430, 551, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 580, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 481, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 395, 511, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 479, 511, 51))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 220, 551, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 320, 551, 41))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 175, 541, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 270, 701, 41))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 375, 551, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 680, 551, 51))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 635, 351, 41))
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 10, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 390, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.encrypt1)
        self.pushButton_2.clicked.connect(self.decrypt1)
        self.pushButton_3.clicked.connect(self.encryptclr)
        self.pushButton_4.clicked.connect(self.decryptclr)

    def encrypt1(self):
        text = self.textEdit.toPlainText()
        key = Fernet.generate_key()  # this is your "password"
        self.plainTextEdit.setPlainText('{}'.format(key))
        cipher_suite = Fernet(key)
        cnvt = bytes(text, "utf-8")
        encoded_text = cipher_suite.encrypt(cnvt)
        self.plainTextEdit_2.setPlainText('{}'.format(encoded_text))

    def decrypt1(self):
        texte = self.textEdit_3.toPlainText()
        keye = self.textEdit_2.toPlainText()
        bkey = bytes(keye, "utf-8")
        cipher_suite = Fernet(bkey)
        code = bytes(texte, "utf-8")
        decoded_text = cipher_suite.decrypt(code)
        self.plainTextEdit_3.setPlainText('{}'.format(decoded_text))

    def encryptclr(self):
        self.textEdit.clear()
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()

    def decryptclr(self):
        self.textEdit_3.clear()
        self.textEdit_2.clear()
        self.plainTextEdit_3.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Click Here To Start Encryption</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "START ENCRYPTION"))
        self.pushButton_2.setText(_translate("MainWindow", "START DECRYPTION"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">ENTER THE TEXT TO ENCRYPT</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "ENTER THE TEXT TO ENCRYPT"))
        self.label_4.setText(_translate("MainWindow", "ENTER THE ENCRYPTED CODE TO DECRYPTED"))
        self.label_5.setText(_translate("MainWindow", "ENTER THE KEY OR PASSWORD WHICH YOU HAVE RECEIVED DURING ENCRYPTION"))
        self.label.setText(_translate("MainWindow", "THIS IS THE KEY/PASSWORD "))
        self.label_2.setText(_translate("MainWindow", "THIS IS THE ENCRYPTED CODE"))
        self.label_6.setText(_translate("MainWindow", "HERE IS THE DECRYPTED CODE"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear All"))
        self.pushButton_4.setText(_translate("MainWindow", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

