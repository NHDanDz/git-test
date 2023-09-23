import csv 
from ListPeople import ListPeople
from People import People
import pandas as pd

# data_to_append = [
#     ['NV0001', 'NHDANZ', '10/10/2003', 'Director', '10000'],
#     ['NV0002', 'NHDANZ1', '10/10/2004', 'Director', '10001'],
#     ['NV0003', 'NHDANZ2', '10/10/2005', 'Director', '10002'],
#     ['NV0004', 'NHDANZ3', '10/10/2006', 'Director', '10003'],
# ]

List = ListPeople()
a = People("12","hai dang", "10/10/2003", "director", "100$")
List.List_People.append(a)
a = People("11","hải do", "11/10/2003", "ditor", "1000$")
List.List_People.append(a)

NewList = List.to_list()

print(NewList)

file = open('my.csv', 'a', newline = '', encoding='utf-8') 
writer = csv.writer(file)
writer.writerows(NewList)
file.close()
# import csv

# def read_csv_to_list_of_dicts(filename):
#     data = []
#     with open(filename, mode='r', newline='', encoding='utf8') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             data.append(row)
#     return data

# filename = 'my.csv'
# people_data = read_csv_to_list_of_dicts(filename)

# # Print the list of dictionaries
# for person in people_data:
#     print(person["EmployeeCode"])
