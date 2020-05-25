#!/bin/bash/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content='''
Model trained successfully. Accuracy reached above 80%
'''
sender_address = 'mansi.dadheech22@gmail.com'
sender_pass = 'Qwerty@123uio'
receiver_address = 'madhusharma311976@gmail.com'
msg = MIMEMultipart()
msg['From'] = sender_address
msg['To'] = receiver_address
msg['Subject'] = 'Testing'
msg.attach(MIMEText(mail_content,'plain'))
session=smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login(sender_address,sender_pass)
text=msg.as_string()
session.sendmail(sender_address,receiver_address,text)
session.quit()
print('Mail Sent')
