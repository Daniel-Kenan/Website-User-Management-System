import smtplib 
 
sender ='accdemo44@gmail.com' 
receivers = ['sdanielkenan@gmail.com'] 
 
message ="""From: From Person <from@fromdomain.com> 
          To: To Person <to@todomain.com> 
          Subject: SMTP e-mail tes"""


try: 
   smtpObj = smtplib.SMTP('localhost') 
   smtpObj.sendmail(sender, receivers, message) 
   print ("Successfully sent email") 
except smtplib.SMTPException: 
   print ("Error: unable to send email")