import employee
from dao import EmployeeDAO
from employee import Employee

dao = EmployeeDAO('employeedb.sqlite')

e = dao.get_by_id(5)
print(e)

e = dao.insert(Employee(230121004, 'Peri', 'Data analyst', '400000', '21-04-2025'))
print(e)

e = dao.get_all()
print(e)

employee = Employee(240221003, 'John', 'Python developer', '300000', '23-09-2020')
e = dao.update(employee)
print(e)

e = dao.delete(240221003, 'John', 'Python developer', '300000', '23-09-2020')
print(e)