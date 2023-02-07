from email.message import EmailMessage

#Create a function to send email
email_sender = "Nnaphichat@gmail.com"
email_pw = "tests"
email_reciever = "Nicolaiaphichat@gmail.com"
import ssl
import smtplib

subject = "Test"
message = "Test"

em = EmailMessage()
em['From'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content(message)

#Create context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pw)
    smtp.sendmail(email_sender, email_reciever, em.as_string())