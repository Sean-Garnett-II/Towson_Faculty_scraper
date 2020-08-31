'''
Created on Aug 30, 2020

@author: SeanGarnett
'''

import requests
import re
from bs4 import BeautifulSoup
from datetime import date

professors = []
url = 'https://www.towson.edu/fcsm/departments/physics/facultystaff/'
data = requests.get('https://www.towson.edu/fcsm/departments/physics/facultystaff/')

soup = BeautifulSoup(data.text, 'html.parser')

fullTime= soup.find('table', {'class': 'table-zebra'})

tbody=fullTime.find('tbody')

for tr in tbody.find_all('tr'):
    username = tr.find_all('td')[0].find_all('a')[0].text.strip()
    email = re.findall(r'(\w+)',tr.find_all('td')[1].find_all('a')[0].text.strip())
    phone = re.findall(r'([0-9]{3}-[0-9]{3}-[0-9]{4})', tr.find_all('td')[1].text.strip())
    room = re.findall(r'([0-9]{3}\-?\w?$)', tr.find_all('td')[1].text.strip())
    professors.append(username + "\n" + email[0] + "@towson.edu" + "\n" + phone[0] + "\n" + "Smith Hall Room "+room[0] + "\n\n")
    
print(*professors, sep = "\n")

saveData = open("Towson Full Time Faculty List", "w+")
saveData.write("A list of Towson's Physic's Department full time faculty and contact information\n\n")
saveData.writelines(professors)
saveData.close()

htmlData = open("HTML site data.txt", "a")
htmlData.write("This is the html data that I scanned when writing this scraper. \nAcquired: ")
htmlData.write(date.today().strftime('%m/%d/%Y'))
htmlData.write("\nfrom ")
htmlData.write(url)
htmlData.write("\n\n\n")
htmlData.writelines(soup.prettify())
htmlData.close()
