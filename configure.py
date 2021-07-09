import os

def local(): 
  with open('emails.txt','r') as local_database:
     return local_database.readlines()

def file():
  if os.path.exists('emails.txt'):
    return local()
  else: 
    open("myfile.txt", "x")
    return local()