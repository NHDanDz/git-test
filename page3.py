# Form implementation generated from reading ui file 'page3.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from ListPeople import ListPeople
from People import People

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 130, 881, 351))
        self.groupBox.setObjectName("groupBox")
        self.push1 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push1.setGeometry(QtCore.QRect(250, 60, 93, 28))
        self.push1.setObjectName("push1")
        self.push2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push2.setGeometry(QtCore.QRect(250, 110, 93, 28))
        self.push2.setObjectName("push2")
        self.push3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push3.setGeometry(QtCore.QRect(250, 160, 93, 28))
        self.push3.setObjectName("push3")
        self.push4 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push4.setGeometry(QtCore.QRect(250, 210, 93, 28))
        self.push4.setObjectName("push4")
        self.push5 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push5.setGeometry(QtCore.QRect(250, 260, 93, 28))
        self.push5.setObjectName("push5")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(50, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(390, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(570, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.push1_1 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push1_1.setGeometry(QtCore.QRect(410, 60, 93, 28))
        self.push1_1.setObjectName("push1_1")
        self.push1_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push1_2.setGeometry(QtCore.QRect(580, 60, 93, 28))
        self.push1_2.setObjectName("push1_2")
        self.push2_1 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push2_1.setGeometry(QtCore.QRect(410, 110, 93, 28))
        self.push2_1.setObjectName("push2_1")
        self.push2_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push2_2.setGeometry(QtCore.QRect(580, 110, 93, 28))
        self.push2_2.setObjectName("push2_2")
        self.push3_1 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push3_1.setGeometry(QtCore.QRect(410, 160, 93, 28))
        self.push3_1.setObjectName("push3_1")
        self.push3_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push3_2.setGeometry(QtCore.QRect(580, 160, 93, 28))
        self.push3_2.setObjectName("push3_2")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(210, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.push4_1 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push4_1.setGeometry(QtCore.QRect(410, 210, 93, 28))
        self.push4_1.setObjectName("push4_1")
        self.push4_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push4_2.setGeometry(QtCore.QRect(580, 210, 93, 28))
        self.push4_2.setObjectName("push4_2")
        self.push5_1 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push5_1.setGeometry(QtCore.QRect(410, 260, 93, 28))
        self.push5_1.setObjectName("push5_1")
        self.push5_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push5_2.setGeometry(QtCore.QRect(580, 260, 93, 28))
        self.push5_2.setObjectName("push5_2")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(720, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.push1_3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push1_3.setGeometry(QtCore.QRect(740, 60, 93, 28))
        self.push1_3.setObjectName("push1_3")
        self.push2_3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push2_3.setGeometry(QtCore.QRect(740, 110, 93, 28))
        self.push2_3.setObjectName("push2_3")
        self.push3_3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push3_3.setGeometry(QtCore.QRect(740, 160, 93, 28))
        self.push3_3.setObjectName("push3_3")
        self.push5_3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push5_3.setGeometry(QtCore.QRect(740, 260, 93, 28))
        self.push5_3.setObjectName("push5_3")
        self.push4_3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.push4_3.setGeometry(QtCore.QRect(740, 210, 93, 28))
        self.push4_3.setObjectName("push4_3")
        self.Home = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(450, 500, 93, 28))
        self.Home.setObjectName("Home")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sorting"))
        self.groupBox.setTitle(_translate("MainWindow", "Sort by:"))
        self.push1.setText(_translate("MainWindow", "Enter"))
        self.push2.setText(_translate("MainWindow", "Enter"))
        self.push3.setText(_translate("MainWindow", "Enter"))
        self.push4.setText(_translate("MainWindow", "Enter"))
        self.push5.setText(_translate("MainWindow", "Enter"))
        self.label_2.setText(_translate("MainWindow", "Employee code"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Date"))
        self.label_5.setText(_translate("MainWindow", "Position"))
        self.label_6.setText(_translate("MainWindow", "Salary"))
        self.label_7.setText(_translate("MainWindow", "InsertionSort"))
        self.label_8.setText(_translate("MainWindow", "QuickSort"))
        self.push1_1.setText(_translate("MainWindow", "Enter"))
        self.push1_2.setText(_translate("MainWindow", "Enter"))
        self.push2_1.setText(_translate("MainWindow", "Enter"))
        self.push2_2.setText(_translate("MainWindow", "Enter"))
        self.push3_1.setText(_translate("MainWindow", "Enter"))
        self.push3_2.setText(_translate("MainWindow", "Enter"))
        self.label_9.setText(_translate("MainWindow", "SelectionSort"))
        self.push4_1.setText(_translate("MainWindow", "Enter"))
        self.push4_2.setText(_translate("MainWindow", "Enter"))
        self.push5_1.setText(_translate("MainWindow", "Enter"))
        self.push5_2.setText(_translate("MainWindow", "Enter"))
        self.label_10.setText(_translate("MainWindow", "MergerSort"))
        self.push1_3.setText(_translate("MainWindow", "Enter"))
        self.push2_3.setText(_translate("MainWindow", "Enter"))
        self.push3_3.setText(_translate("MainWindow", "Enter"))
        self.push5_3.setText(_translate("MainWindow", "Enter"))
        self.push4_3.setText(_translate("MainWindow", "Enter"))
        self.Home.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())