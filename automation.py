import pandas as pd
import requests
from bs4 import BeautifulSoup
page=requests.get('https://forecast.weather.gov/MapClick.php?lat=34.0536&lon=-118.2455')
soup=BeautifulSoup(page.content,'html.parser')
week=soup.find(id='seven-day-forecast-body')
#print(week)
items=week.find_all(class_='tombstone-container')
#print(items[2])
# print(items[0].find(class_="period-name").get_text())
# print(items[1].find(class_='short-desc').get_text())  #ctrl+K+c
# print(items[1].find(class_="temp").get_text())
#we will use List_comphrension
# period_names=[item.find(class_='period-name').get_text() for item in items]
# print(period_names)
#short_description=[item.find(class_='short-desc').get_text() for item in items if item!=None]
#print(short_description)
period_names=[]
for i in range(0,len(items)):
      period_names.append(items[i].find(class_='period-name').get_text())
#print(period_names)
#print()
short_des=[]
for i in range(0,len(items)):
      short_des.append(items[i].find(class_='short-desc').get_text())

#print(short_des)
#print()
tempe=[]

for i in range(0,len(items)):
      tempe.append(items[i].find(class_='temp').get_text())

#print(tempe)
weather_stuffs=pd.DataFrame({
    'Period':period_names,
    'short_description':short_des,
    'Temperature':tempe

})
print(weather_stuffs)
weather_stuffs.to_csv('weather3.csv')