# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(388, 212)
        Dialog.setMinimumSize(QtCore.QSize(388, 212))
        Dialog.setMaximumSize(QtCore.QSize(388, 212))
        Dialog.setWindowOpacity(1.0)
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(0, 0, 381, 41))
        font = QtGui.QFont()
        font.setFamily("a_Simpler3D")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setTextFormat(QtCore.Qt.AutoText)
        self.Title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Title.setObjectName("Title")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 371, 121))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.filechoose1 = QtWidgets.QPushButton(self.groupBox)
        self.filechoose1.setGeometry(QtCore.QRect(330, 30, 31, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.filechoose1.setFont(font)
        self.filechoose1.setObjectName("filechoose1")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_1.setObjectName("label_1")
        self.directory1 = QtWidgets.QTextEdit(self.groupBox)
        self.directory1.setEnabled(True)
        self.directory1.setGeometry(QtCore.QRect(20, 30, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.directory1.setFont(font)
        self.directory1.setAcceptDrops(False)
        self.directory1.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.directory1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.directory1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.directory1.setReadOnly(True)
        self.directory1.setObjectName("directory1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.directory2 = QtWidgets.QTextEdit(self.groupBox)
        self.directory2.setEnabled(True)
        self.directory2.setGeometry(QtCore.QRect(20, 80, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.directory2.setFont(font)
        self.directory2.setAcceptDrops(False)
        self.directory2.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.directory2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.directory2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.directory2.setReadOnly(True)
        self.directory2.setObjectName("directory2")
        self.filechoose2 = QtWidgets.QPushButton(self.groupBox)
        self.filechoose2.setGeometry(QtCore.QRect(330, 80, 31, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.filechoose2.setFont(font)
        self.filechoose2.setObjectName("filechoose2")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(250, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("a_Simpler3D")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.load = QtWidgets.QPushButton(Dialog)
        self.load.setGeometry(QtCore.QRect(110, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("a_Simpler3D")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.load.setFont(font)
        self.load.setObjectName("load")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ultra Super Cool TeleGram Joiner 2000"))
        self.Title.setText(_translate("Dialog", "USCTGSJOINER 2000"))
        self.filechoose1.setText(_translate("Dialog", "..."))
        self.label_1.setText(_translate("Dialog", "Target groups"))
        self.directory1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose file...</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Log output"))
        self.directory2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose folder...</p></body></html>"))
        self.filechoose2.setText(_translate("Dialog", "..."))
        self.start.setText(_translate("Dialog", "Start"))
        self.load.setText(_translate("Dialog", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
