import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read employee information from JSON file
with open('employee.json', 'r') as file:
    data = json.load(file)

# Create a list of Employee objects
employees = []
for employee_info in data['employees']:
    employee = Employee(
        employee_info['Name'],
        employee_info['DOB'],
        employee_info['Height'],
        employee_info['City'],
        employee_info['State']
    )
    employees.append(employee)

# Print the list of Employee objects
for employee in employees:
    print("Name:", employee.name)
    print("DOB:", employee.dob)
    print("Height:", employee.height)
    print("City:", employee.city)
    print("State:", employee.state)
    print()

import json

# Dictionary of Indian states and capitals
states_capitals = {
    "Andhra Pradesh": "Hyderabad",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai"
}

with open('states_capitals.json', 'w') as file:
    json.dump(states_capitals, file)


