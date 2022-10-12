from time import sleep
from django.core.mail import send_mail
from celery import shared_task
import os
import smtplib
from email.mime.text import MIMEText

@shared_task()
def send_feedback_email_task(sender, subject, message):

    password = os.getenv("EMAIL_PASSWORD")   
    localemail = "emailsenderinform@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(localemail, password)
    msg =  MIMEText(message)
    msg["Subject"] = subject

    sleep(20)  
               

    server.sendmail(localemail, sender, msg.as_string())

  
    