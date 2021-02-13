import email, smtplib, ssl
import messagebuilder
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendSingle(nameParam):

    emails = []
    names = []
    filepath = "store.txt"
    f = open(filepath, "r")

    for x in f:
        line = x.replace("\n", "")
        email = line.split(", ")[0].strip()
        name = line.split(", ")[1].strip()
        emails.append(email)
        names.append(name)
    
    for i in range(len(names)):
        if names[i].lower() == nameParam.lower():
            print("sending to: " + emails[i])
            deliver(emails[i], names[i])

def sendAll():

    emails = []
    names = []
    filepath = "store.txt"
    f = open(filepath, "r")

    for x in f:
        line = x.replace("\n", "")
        email = line.split(", ")[0].strip()
        name = line.split(", ")[1].strip()
        emails.append(email)
        names.append(name)

    for i in range(len(names)):
        print("sending to: " + emails[i])
        deliver(emails[i], names[i])

def deliver(receiver_email, receiver_name):
    
    subject = messagebuilder.getSubject()
    body = messagebuilder.buildMessage(receiver_name)

    sender_email = messagebuilder.getSenderEmail()
    password = messagebuilder.getPass()
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))
    text = message.as_string()
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

def deliverBcc(bcc_emails):
    
    subject = messagebuilder.getSubject()
    body = messagebuilder.buildBCC()

    sender_email = messagebuilder.getSenderEmail()
    password = messagebuilder.getPass()
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Bcc"] = bcc_emails
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))
    text = message.as_string()
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, bcc_emails, text)
