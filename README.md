In my code, you can see the first class, calles as Employee. With the class, I can create employee objects with attributes such as employee id, name, position, salary, and hire date.
The salary attribute is not accessible. In the Employee class, there are are such methods as set salary, since salary is private; get salary (in order to get the salary information); and 
str magic method, that displays all the information about an employee object.
ini
In dao file I created EmployeeDAO class, where Data Access Object may be created. I have an init magic method, where I created attributes such as self.conn, in order to have a connection to my database, 
and self.cursor, in order to make changes to the database. Using the corresponding methods in the class, you can get an employee from the database by their id; you can get all employees from the 
database, insert new employees, update the existing employee and delete any employee.

TEST OUTPUTS
![Снимок экрана 2025-04-08 122022](https://github.com/user-attachments/assets/c260f794-3916-44c4-9967-817cc5b2576c)

EMPLOYEE DATABASE
![Снимок экрана 2025-04-08 122045](https://github.com/user-attachments/assets/4d09f9b9-f805-4115-be43-6ad72d6d5cc7)
Here, you can see, that the employee with id:2 is deleted, and 5th employee was updated, and inserted new employee with id:21.
