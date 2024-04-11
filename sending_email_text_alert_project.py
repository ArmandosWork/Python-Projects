#With this program, one can send Email/SMS Text alert messages via Gmail SMTP to a given email or Phone.

import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body) #Method
    msg['subject'] = subject
    msg['to'] = to

    user = "youremail@gmail.com"
    msg['from'] = user
    password = "xxxx xxxx xxxx xxxx" #Password or App Pass.

    #Server Settings:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() 
    server.login(user, password) 
    server.send_message(msg)

    server.quit()

if __name__ == '__main__': #This tests to see if this code is run on this program; not on other programs.

    email_alert("Hello, there!", "This is your PY Alert.", "xxxxxxxxxx@goodemail.com")
    #For emails, use any good email address.
    #For Text messages, use :numberXXX@tmomail.net (This example would be for a T-Mobile phone). Do a Google search for your given carrier.
