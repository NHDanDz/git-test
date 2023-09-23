import math
from People import People

class ListPeople:
    List_People = [] 
    # Hàm tạo ID tăng dần cho nhân viên
    def sortByID(self):
        self.List_People.sort(key=lambda x: x.EmCode, reverse=False)
    def sortByName(self):
        self.List_People.sort(key=lambda x: x.Name, reverse=False)
    def sortByDate(self):
        self.List_People.sort(key=lambda x: x.Date, reverse=False)        
    def sortByPos(self):
        self.List_People.sort(key=lambda x: x.Pos, reverse=False)
    def sortBySal(self):
        self.List_People.sort(key=lambda x: x.Sal, reverse=False)
    def NumPeople(self):
        return self.List_People.__len__() 
    def insertion_sort(self, field):
        n = self.NumPeople()
        people = self.List_People
        for i in range(n):
            current_person = people[i]
            j = i - 1
            while j >= 0 and getattr(current_person, field) < getattr(people[j], field):
                people[j + 1] = people[j]
                j -= 1
            people[j + 1] = current_person

    def selection_sort(self, field):
        n = self.NumPeople()
        people = self.List_People
        for i in range(n - 1):
            min_index = int(i)
            for j in range(i + 1, n):
             # So sánh theo trường field
                if field == 'EmCode' and people[j].EmCode < people[min_index].EmCode:
                    min_index = j
                elif field == 'Name' and people[j].Name < people[min_index].Name:
                    min_index = j
                elif field == 'Date' and people[j].Date < people[min_index].Date:
                    min_index = j
                elif field == 'Pos' and people[j].Pos < people[min_index].Pos:
                    min_index = j
                elif field == 'Sal' and people[j].Sal < people[min_index].Sal:
                    min_index = j
        # Hoán đổi vị trí của hai đối tượng
            people[i], people[min_index] = people[min_index], people[i] 
    
    def quicksort(self, arr, field):
        
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = []
        middle = []
        right = []
        
        for person in arr:
            if getattr(person, field) < getattr(pivot, field):
                left.append(person)
            elif getattr(person, field) == getattr(pivot, field):
                middle.append(person)
            else:
                right.append(person) 
        ans = []
        ans = self.quicksort(left, field) + middle + self.quicksort(right, field)
        return ans

    def merge_sort(self, people, field):
        if len(people) <= 1:
            return people
        
        # Chia danh sách thành hai nửa
        middle = len(people) // 2
        left = people[:middle]
        right = people[middle:]
        
        # Gọi đệ quy cho cả hai nửa
        left = self.merge_sort(left, field)
        right = self.merge_sort(right, field)
        
        # Hợp nhất hai nửa đã sắp xếp lại thành một danh sách đã sắp xếp
        return self.merge(left, right, field)

    def merge(self, left, right, field):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if getattr(left[i], field) < getattr(right[j], field):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    def sequential_search(self, field, value):
        for person in self.List_People:
            if getattr(person, field) == value:
                return person  # Trả về đối tượng nếu tìm thấy 

    def binary_search(self, field, value):
        # Đảm bảo danh sách đã được sắp xếp trước
        # self.showInfo()
        NewList = self.List_People
        left = 0
        right = len(NewList) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = getattr(NewList[mid], field)

            if mid_value == value:
                return NewList[mid]  # Tìm thấy giá trị, trả về đối tượng tương ứng
            elif mid_value < value:
                left = mid + 1
            else:
                right = mid - 1
        # print("--------------Final-------------\n")
        # self.showInfo()
        return None  # Không tìm thấy giá trị, trả về None

    def Search(self, ID):
        for person in self.List_People:
            if person.EmCode == ID:
                return person 
        return None
    def showInfo(self):
        for person in self.List_People:
            print("Employee Code:", person.EmCode)
            print("Name:", person.Name)
            print("Date:", person.Date)
            print("Position:", person.Pos)
            print("Salary:", person.Sal)
            print("\n")  # In một dòng trống để phân biệt giữa các phần tử
    def to_list(self):
        people_list = []
        for person in self.List_People:
            person_dict = [
                person.EmCode,
                person.Name,
                person.Date,
                person.Pos,
                person.Sal
            ]
            people_list.append(person_dict)
        return people_list
# List = ListPeople()
# a = People("12","hai dang", "10/10/2003", "director", "100$")
# List.List_People.append(a)
# a = People("11","hai do", "11/10/2003", "ditor", "1000$")
# List.List_People.append(a)
# # Duyệt từng phần tử của danh sách List_People
# List.showInfo()

# List.sortByID() 
