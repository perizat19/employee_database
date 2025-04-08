import sqlite3
from employee import Employee


class EmployeeDAO():

    def __init__(self, databasefile):
        self.conn = sqlite3.connect(databasefile)
        self.cursor = self.conn.cursor()

    def get_by_id(self, id):
        sql = '''
            SELECT *
            FROM employee
            WHERE id = ?
        '''

        self.cursor.execute(sql, (id,))
        row = self.cursor.fetchone()

        if row:
            employee = Employee(employee_id=row[0], name=row[1], position=row[2], salary=row[3], hire_date=row[4])
        else:
            employee = None

        return employee

    def insert(self, employee: Employee):
        sql = '''
            INSERT INTO employee (name, position, salary, hire_date)
            VALUES (?, ?, ?, ?);
        '''

        self.cursor.execute(sql, (employee.name, employee.position, employee._salary,employee.hire_date))
        id = self.cursor.lastrowid
        self.conn.commit()
        return id

    def get_all(self):
        sql = '''
            SELECT *
            FROM employee;
        '''
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            employee = Employee(employee_id=row[0], name=row[1], position=row[2], salary=row[3], hire_date=row[4])
            return employee

    def update(self, employee:Employee):
        sql = '''
            UPDATE employee (name, position, salary, hire_date)
            SET name=?, position=?, salary=?, hire_date=? 
            WHERE id = ?; 
        '''
        self.cursor.execute(sql, (employee.name, employee.position, employee.salary,
                                  employee.hire_date, employee.employee_id))
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, id):
        sql = '''
            DELETE FROM employee
            WHERE id = ? ;
        '''
        self.cursor.execute(sql, (id,))
        self.conn.commit()
        return self.cursor.rowcount
