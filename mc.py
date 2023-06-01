import csv, smtplib, ssl
message = """Subject: dispatch id
Hi {name}, your dispatch id is {dispatchid}"""
from_address = "gottipatisaividhya4280@gmail.com"
password = "sxrn expn krbu ajkl"
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for name, email, dispatchid in reader:
            server.sendmail(from_address,email,message.format(name=name,dispatchid=dispatchid),)
    