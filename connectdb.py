import mysql.connector
db = mysql.connector.connect(user = 'root', password = '123456', host = 'localhost', database = 'qlnv')
#QUERY
code = 'CREATE database `qlnv` ;'
#Create table
code1 = "CREATE TABLE `company` (`EmployyCode` VARCHAR(45) NOT NULL,`Name` VARCHAR(45) NOT NULL,`Date` VARCHAR(45) NOT NULL,`Position` VARCHAR(45) NOT NULL,`Salary` VARCHAR(45) NOT NULL,PRIMARY KEY (`EmployyCode`));"
#RUN

mycursor = db.cursor()
mycursor.execute(code1)