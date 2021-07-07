from email import message
import smtplib 
from email.message import EmailMessage
import easyimap as e

class mailing_system:
    
    def __init__(self,email, password):
        self.password = password
        self.email = email
    
    def readMail(self):
        server = e.connect("imap.gmail.com",self.email,self.password)
        print(server.mail(server.listids()[0]).body)

    def sendMail(self,Subject, To, Body):

        msg = EmailMessage()
        msg['From'] = self.email
        msg["Subject"] = Subject
        msg["To"] = To
        msg.set_content(Body)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
              smtp.login(self.email,self.password)
              smtp.send_message(msg)




# account.mail(To = 'sdanielkenan@gmail.com' , Subject = "hello", Body ="hello world")
