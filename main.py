# creating a payroll system
class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name= name
        self.salary = salary
    def calculate_salary(self):
        pass
class HourlyEmployee(Employee):
        def __init__(self, emp_id,name,salary,hourly_rate, hours_worked):
            super().__init__(emp_id,name,salary)
            self.hourly_rate = hourly_rate
            self.hours_worked = hours_worked

        def calculate_salary(self):
            return self.hours_worked * self.hourly_rate
class SalariedEmployee(Employee):
    def __init__(self, emp_id,name,salary,monthly_salary):
        super().__init__(emp_id, name, salary)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary

employee_types = {
    'hourly': HourlyEmployee,
    'salaried': SalariedEmployee
}

emp_id = int(input('Enter employee ID: '))
name = input('Enter your name: ')
employee_type = input('Enter employee type (Hourly or Salaried): ').lower()

if employee_type in employee_types:
    if employee_type == 'hourly':
        hours_worked = int(input('Enter Hours worked: '))
        hourly_rate = float(input('Enter hourly rate: '))
        salary = employee_types[employee_type](emp_id, name, 0, hourly_rate, hours_worked)
    elif employee_type == 'salaried':
        monthly_salary = float(input('Enter monthly salary: '))
        salary = employee_types[employee_type](emp_id, name, 0, monthly_salary)

    print('Employee name:', salary.name)
    print('Employee ID:', salary.emp_id)
    print('Salary:', salary.calculate_salary())
else:
    print("Invalid employee type!")


