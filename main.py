from PyQt6 import QtGui, QtWidgets, QtCore
import sys
import home, test, page2, page3, page4 
from ListPeople import ListPeople
from People import People
import csv
#process

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

List = ListPeople()

def homeUI():
    global ui
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Page1.clicked.connect(page1UI) 
    ui.Page2.clicked.connect(lambda: page2UI('home'))
    ui.Page3.clicked.connect(page3UI) 
    ui.Page4.clicked.connect(page4UI)  
    #global list
    #print(list)
    MainWindow.show()

def page1UI(): 
    global ui
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    global List
    ui.Home.clicked.connect(ui.get_Info) 
    ui.Home.clicked.connect(homeUI) 
    MainWindow.show()

def page2UI(Info):
    global ui, List 
    ui = page2.Ui_MainWindow() 
    ui.setupUi(MainWindow, List)
    if Info == "home":
        ui.Home.clicked.connect(homeUI)
    if Info == "page3UI":
        ui.Home.clicked.connect(page3UI)
    MainWindow.show()

def Type1():
    List.selection_sort('EmCode')
    page2UI("page3UI")

def Type2():
    List.selection_sort('Name')
    page2UI("page3UI")

def Type3():
    List.selection_sort('Date')
    page2UI("page3UI")
    
def Type4():
    List.selection_sort('Pos')
    page2UI("page3UI")
    
def Type5():
    List.selection_sort('Sal')
    page2UI("page3UI")
    
def Type1_1():
    List.insertion_sort('EmCode')
    page2UI("page3UI")

def Type2_1():
    List.insertion_sort('Name')
    page2UI("page3UI")

def Type3_1():
    List.insertion_sort('Date')
    page2UI("page3UI")

def Type4_1():
    List.insertion_sort('Pos')
    page2UI("page3UI")

def Type5_1():
    List.insertion_sort('Sal')
    page2UI("page3UI")        
     
def Type1_2(): 
    global List
    List.List_People = List.quicksort(List.List_People, 'EmCode') 
    page2UI("page3UI")
 
def Type2_2(): 
    global List
    List.List_People = List.quicksort(List.List_People, 'Name') 
    page2UI("page3UI")

def Type3_2(): 
    global List
    List.List_People = List.quicksort(List.List_People, 'Date') 
    page2UI("page3UI")

def Type4_2(): 
    global List
    List.List_People = List.quicksort(List.List_People, 'Pos') 
    page2UI("page3UI")

def Type5_2(): 
    global List
    List.List_People = List.quicksort(List.List_People, 'Sal') 
    page2UI("page3UI")
    
def Type1_3():
    global List
    List.List_People = List.merge_sort(List.List_People, 'EmCode') 
    page2UI("page3UI")    
    
def Type2_3():
    global List
    List.List_People = List.merge_sort(List.List_People, 'Name') 
    page2UI("page3UI")    

def Type3_3():
    global List
    List.List_People = List.merge_sort(List.List_People, 'Date') 
    page2UI("page3UI")    

def Type4_3():
    global List
    List.List_People = List.merge_sort(List.List_People, 'Pos') 
    page2UI("page3UI")    

def Type5_3():
    global List
    List.List_People = List.merge_sort(List.List_People, 'Sal') 
    page2UI("page3UI")    
        
def page3UI():
    global ui
    ui = page3.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.push1.clicked.connect(Type1)
    ui.push2.clicked.connect(Type2)
    ui.push3.clicked.connect(Type3)
    ui.push4.clicked.connect(Type4)
    ui.push5.clicked.connect(Type5)
    ui.push1_1.clicked.connect(Type1_1)
    ui.push2_1.clicked.connect(Type2_1)
    ui.push3_1.clicked.connect(Type3_1)
    ui.push4_1.clicked.connect(Type4_1)
    ui.push5_1.clicked.connect(Type5_1)
    ui.push1_2.clicked.connect(Type1_2)
    ui.push2_2.clicked.connect(Type2_2)
    ui.push3_2.clicked.connect(Type3_2)
    ui.push4_2.clicked.connect(Type4_2)
    ui.push5_2.clicked.connect(Type5_2)
    ui.push1_3.clicked.connect(Type1_3)
    ui.push2_3.clicked.connect(Type2_3)
    ui.push3_3.clicked.connect(Type3_3)
    ui.push4_3.clicked.connect(Type4_3)
    ui.push5_3.clicked.connect(Type5_3)
    ui.Home.clicked.connect(homeUI)
    MainWindow.show()


def page4UI():
    global ui, List  
    ui = page4.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.push1.clicked.connect(lambda: ui.Searching(List, 'EmCode'))
    ui.push2.clicked.connect(lambda: ui.Searching(List, 'Name'))
    ui.push3.clicked.connect(lambda: ui.Searching(List, 'Date'))
    ui.push4.clicked.connect(lambda: ui.Searching(List, 'Pos'))
    ui.push5.clicked.connect(lambda: ui.Searching(List, 'Sal'))
    ui.push1_1.clicked.connect(lambda: ui.BinarySearching(List, 'EmCode'))
    ui.push1_2.clicked.connect(lambda: ui.BinarySearching(List, 'Name'))
    ui.push1_3.clicked.connect(lambda: ui.BinarySearching(List, 'Date'))
    ui.push1_4.clicked.connect(lambda: ui.BinarySearching(List, 'Pos'))
    ui.push1_5.clicked.connect(lambda: ui.BinarySearching(List, 'Sal'))
    ui.Home.clicked.connect(homeUI)
    MainWindow.show()

def loadfile():
    data = []
    global List
    filename = 'my.csv'
    with open(filename, mode='r', newline='', encoding='utf8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
            NewOne = People(row['EmployeeCode'], row['Name'], row['Date'], row['Position'], row['Salary'])  
            List.List_People.append(NewOne)  
    return None

#run 
loadfile()
List.showInfo()
homeUI() 
sys.exit(app.exec())