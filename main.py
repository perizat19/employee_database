import employee
from dao import EmployeeDAO
from employee import Employee

dao = EmployeeDAO('employeedb.sqlite')

e = dao.get_by_id(5)
print(f'Get by id: \n{e}')

e = dao.insert(Employee(230121004, 'Peri', 'Data analyst', '400000', '21-04-2025'))
print(f'Insert:\n {e}')

e = dao.get_all()
print(f'Get all:\n {e}')

employee = Employee(5, 'John', 'Python developer', '300000', '23-09-2020')
e = dao.update(employee)
print(f'Updated: {e}')

e = dao.delete(2)
print(e)
