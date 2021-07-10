from manageMail import initialise
import requests
from bs4 import BeautifulSoup
from configure import file
import os 
from time import sleep

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

    def watch(self,url):
        # varialble = 
        while True:
           if url.status_code  == 200:

               pass
            #   email website is down ND PROVIDES time  
           else:
               pass
            # website is up and running   
        sleep(5000)   

    def urlPublish():
        # publish data of the site
        pass

    def scrape(url):
        # scrape website and send the data by email if email or store data on the txt
        pass

    def pdfSite():
        pass