from datetime import datetime

import mysql.connector
from sqlalchemy.ext.indexable import index_property

mydb = mysql.connector.connect(
    host="35.240.151.115",
    port="3306",
    user="astar",
    passwd="a1s2d3f4g5h6j7k8l9!",
    database='digiEmoV2ForVirusData'
)
print(mydb.database)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM news;')
myresult = mycursor.fetchall()

import pandas as pd

data = pd.DataFrame(columns=['Title', 'URL', 'Date', 'Time', 'Channel'])


def get_date(date):
    pass


def get_time(date):
    date = date.replace('+08:00 SGT', '')
    try:
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        t = date.strftime('%H:%M:%S')
        day = date.strftime('%d-%m-%Y')
        # with open('dates.txt', 'a+') as f:
        #     f.write(date + '\n')
        # print(type(date))
    except Exception as e:
        print(date)
        print(e)
        exit(0)
    return t, day


i = 1
for x in myresult:
    print(x)
    title = x[0]
    title = title.replace('“', '\'')
    title = title.replace('”', '\'')
    url = x[1]
    time, date = get_time(x[2])
    channel = x[3]
    data.loc[i] = [title, url, date, time, channel]
    i += 1

data.to_csv('from_db.csv', index_label='Index')
data.to_excel('from_db.xlsx', index_label='Index')

print(len(myresult))
