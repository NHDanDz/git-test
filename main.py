from PyQt6 import QtGui, QtWidgets, QtCore
import sys
import home, test, page2 

#process

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

List = []


def homeUI():
    global ui
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Page1.clicked.connect(page1UI) 
    ui.Page2.clicked.connect(page2UI) 
    #global list
    #print(list)
    MainWindow.show()

def page1UI(): 
    global ui
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    global List
    ui.Home.clicked.connect(ui.get_Info)
    List = test.List  
    ui.Home.clicked.connect(homeUI) 
    MainWindow.show()

def page2UI():
    global ui, List 
    ui = page2.Ui_MainWindow()
    ui.setupUi(MainWindow, List)
    ui.Home.clicked.connect(homeUI)
    MainWindow.show()
#run 
homeUI() 
sys.exit(app.exec())