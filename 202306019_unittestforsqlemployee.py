import unittest
import os
from dotenv import load_dotenv
from sqlemail_202306014 import EmailDatabase
import time

class EmailDatabaseTest(unittest.TestCase):
   
    def setUp(self):
        load_dotenv()
        host_name = os.environ['host_name']
        user_name = os.environ['user_name']
        database_password = os.environ['database_password']
        database_name1 = os.environ['database_name1']

        self.db = EmailDatabase(host_name, user_name, database_password, database_name1)
        self.db.connect()
        self.db.create_table()
  
    def tearDown(self): 
        self.db.delete_emails()
        self.db.disconnect()
  
    def get_unique_id(self):
        query = "SELECT IFNULL(MIN(id), 0) FROM emails"
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchone()
        print("Query:", query)
        print("Result:", result)
        unique_id = result['IFNULL(MIN(id), 0)'] + 1
        return  unique_id

    def test_insert_emails(self):
        subject = 'JUICE SALON MEMBERSHIP ACTIVATION'
        body = """Dear Customer,
             Thank you for choosing us."""
        
        
    
        
        #self.db.insert_emails( 'automatedemail@gmail.com', subject, body)


        emails = self.db.get_all_emails()
        print(emails)
        self.assertEqual(len(emails), 1)
        self.assertEqual(emails[0]['receiver'],'automatedemail@gmail.com')
        self.assertEqual(emails[0]['subject'], subject)
        self.assertEqual(emails[0]['body'], body)
    

if __name__ == '__main__':
    unittest.main()
