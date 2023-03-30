'''Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information
  consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file 
  and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.'''

import json

class Employee:
    def __init__(self, name, DOB, height, city, state):
        self.name = name
        self.DOB = DOB
        self.height = height
        self.city = city
        self.state = state

with open("employee.json") as file:
    json_object = json.load(file)

#Taking input for employee ID to show that particular emoployee only 
emp = input('''Enter the emp ID (i.e '1', '2', '3', '4','5'): ''')
obj = Employee(json_object[emp]['name'], json_object[emp]['DOB'],json_object[emp]['height'],json_object[emp]['city'],json_object[emp]['state'])

print(json_object[emp]) # It will print all employee details
print(obj.name) # It will print name information of specific employee ID we enter during input
print(obj.DOB) # It will print DOB information of specific employee ID we enter during input
print(obj.height) # It will print height information of specific employee ID we enter during input
print(obj.city) # It will print city information of specific employee ID we enter during input
print(obj.state) # It will print state information of specific employee ID we enter during input

