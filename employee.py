class Employee():

    def __init__(self, employee_id, name, position, salary, hire_date):

        self.employee_id = employee_id
        self.name = name
        self.position = position
        self._salary = salary
        self.hire_date = hire_date

    def __str__(self):

        return (f'Employee id: {self.employee_id}\n'
                f'Name: {self.name}\n'
                f'Position: {self.position}\n'
                f'Hire date: {self.hire_date}')

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    @property
    def salary(self):
        return self._salary

