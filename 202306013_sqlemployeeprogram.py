import pymysql.cursors
from dotenv import load_dotenv
import os


class EmployeeDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = pymysql.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          database=self.database,
                                          cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT,
            designation VARCHAR(255)
        )
        '''
        self.cursor.execute(query)
        self.connection.commit()

    def insert_employee(self, name, age, designation):
        query = '''
        INSERT INTO employees (name, age, designation)
        VALUES (%s, %s, %s)
        '''
        self.cursor.execute(query, (name, age, designation))
        self.connection.commit()

    def get_all_employees(self):
        query = '''
        SELECT * FROM employees
        '''
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    def update_employee(self, id, name, age, designation):
        query = """UPDATE employees
                SET name=%s, age=%s, designation=%s
                WHERE id=%s"""
        self.cursor.execute(query,(name, age, designation, id))
        self.connection.commit()
    
    def delete_employee(self, id):
        query= """DELETE FROM employees
               WHERE id=%s"""
        self.cursor.execute(query,(id))
        self.connection.commit()

    def disconnect(self):
        if self.connection and self.cursor:
            self.cursor.close()
            self.connection.close()
            self.cursor = None
            self.connection = None

def main():
    load_dotenv()
    host_name = os.environ['host_name']
    user_name = os.environ['user_name']
    database_password = os.environ['database_password']
    database_name = os.environ['database_name']

    db = EmployeeDatabase(host_name, user_name, database_password, database_name)
    db.connect()
    db.create_table()

    
    db.insert_employee('John Doe', 25, 'Software Engineer')

    employees = db.get_all_employees()
    print("All Employees:")
    print(employees)
    
    db.update_employee(2,'Saividhya', 20, 'developer')
    db.delete_employee(6)
    
   
  
    db.disconnect()

if __name__ == '__main__':
    main()
