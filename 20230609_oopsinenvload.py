from email.message import EmailMessage
from dotenv import load_dotenv
import os
import ssl
import smtplib
class Email:
    def __init__(self):
        load_dotenv()
        self.email_sender = os.environ['EMAIL_ADDRESS']
        self.email_password = os.environ['EMAIL_PASSWORD']
    def send_email(self, email_receiver, subject, body):
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
          smtp.login(self.email_sender, self.email_password)
          smtp.send_message(em)
email_sender = Email()
email_receiver = 'gottipatisaividhya4280@gmail.com'
subject = 'test mail'
body = """
generating a automated mail using python"""
email_sender.send_email(email_receiver, subject, body)

