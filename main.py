from manageMail import initialise
import requests
from bs4 import BeautifulSoup
from configure import file
import os 

email = 'accdemo44@gmail.com'
pasword = os.environ.get('PASSWORDPORTFOLIO')
url = requests.get('https://beautiful-soup-4.readthedocs.io/en/latest/')


account = initialise(email=email, password=pasword)


class WUMS:
    
    def __init__(self, email , password, url , Subject):
          self.email = email
          self.password = password
          _url = requests.get(url)
          self.html = _url.text
          self.Subject = Subject
    
    @property
    def htmlContent(self):
        html = self.html
        return BeautifulSoup(html,'html.parser').get_text()

    def notify(self):
       email =  self.email
       password = self.password
       account = initialise(email = email, password = password)
       
       for email in  file():
           account.sendMail(To = email , Subject = "hello", Body = self.htmlContent)
