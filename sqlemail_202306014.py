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
                   id BIGINT AUTO_INCREMENT PRIMARY KEY
                   )"""
        self.cursor.execute(query)
        self.connection.commit()
   
    def insert_emails(self, recipientname, employeeid, receiver):
        query = """INSERT INTO emails( recipientname, employeeid, receiver)
                VALUES(%s,%s,%s)"""
        self.cursor.execute(query,( recipientname, employeeid, receiver))
        self.connection.commit()
    
    def get_all_emails(self):
        query = "SELECT * FROM emails ORDER BY id DESC LIMIT 1"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        emails = []
        for row in result:
            email = {
            "id": row['id'],
            "recipientname": row['recipientname'],
            "employeeid": row['employeeid'],
            "receiver": row['receiver'],
            }
            emails.append(email)
        return emails
    
     
     
    #def column_add(self):
        query="""ALTER TABLE emails 
               ADD column employeeid BIGINT AFTER recipientname"""
        self.cursor.execute(query)
        self.connection.commit()
    
    #def column_delete(self):
        query="""ALTER TABLE emails
                DROP column body """
        self.cursor.execute(query)
        self.connection.commit()
              
    
    def delete_emails(self,id):
        query= """DELETE FROM emails
               Where id = %s"""
        self.cursor.execute(query,(id))
        self.connection.commit()
    
    def update_emails(self,id, recipientname, employeeid):
        query= """UPDATE emails 
               SET recipientname=%s, employeeid=%s 
               WHERE id=%s"""
        self.cursor.execute(query,(recipientname, employeeid, id))
        self.connection.commit()    
    
    #def auto_increment(self):
        #query="""ALTER TABLE emails AUTO_INCREMENT=1"""
        #self.cursor.execute(query)
        #self.connection.commit()
    
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
    db.create_table()
    
   

        
   
    

    db.insert_emails('anu', 45689, 'gottipatisaividhya4280@gmail.com')
    
    #db.column_add()
    #db.column_delete()
    
    emails = db.get_all_emails()
    print("ALL EMAILS:")
    print(emails)
    
    #db.update_emails(37, subject, body )

    #db.auto_increment()

    #db.delete_emails(34)

    db.disconnect()

if __name__ == '__main__':
    main()