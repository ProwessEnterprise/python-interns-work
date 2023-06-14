import pymysql.cursors
from dotenv import load_dotenv
import os


class EmailDatabase:
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
        query = """CREATE TABLE IF NOT EXISTS emails(
                   id INT  PRIMARY KEY,
                   subject VARCHAR(255),
                   body text )"""
        self.cursor.execute(query)
        self.connection.commit()
   
    def insert_emails(self, id, receiver, subject, body):
        query = """INSERT INTO emails(id, receiver, subject, body)
                VALUES(%s,%s,%s, %s)"""
        self.cursor.execute(query,(id, receiver, subject, body))
        self.connection.commit()
    
    def get_all_emails(self):
        query="""SELECT * FROM emails"""
        self.cursor.execute(query)
        result=self.cursor.fetchall()
        return result
    
    #def column_add(self):
        query="""ALTER TABLE emails 
               ADD column receiver VARCHAR(225) AFTER id"""
        self.cursor.execute(query)
        self.connection.commit()
    
    #def delete_emails(self,id):
        query= """DELETE FROM emails
                WHERE id=%s"""
        self.cursor.execute(query,(id))
        self.connection.commit()
    
    # def auto_increment(self):
        query="""ALTER TABLE emails AUTO_INCREMENT=1"""
        self.cursor.execute(query)
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
    database_name1 = os.environ['database_name1']

    db = EmailDatabase(host_name, user_name, database_password, database_name1)
    db.connect()
    #db.create_table()

    #db.insert_emails(1,'gottipatisaividhya4280@gmail.com','AUTOMATED EMAILS','sending emails through sql')
    db.insert_emails(2,'sgottipa@gitam.in','AUTOMATED EMAILS','sending emails through sql')
    
    #db.column_add()
    
    emails = db.get_all_emails()
    print("ALL EMAILS:")
    print(emails)

    #db.auto_increment()

    #db.delete_emails(1)

    db.disconnect()
if __name__ == '__main__':
    main()
