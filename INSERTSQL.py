#!/usr/bin/python3
#coding: utf8

import requests
import json
import time
import datetime
import configparser

config = configparser.ConfigParser()
config.read('/home/pi/Python/config.ini')

HOST = config['mysql']['host']
USER = config['mysql']['user']
PASSWD = config['mysql']['passwd']
DB = config['mysql']['db']

token = config['awattar']['TOKEN']
URL = config['awattar']['URL']

#print('aWATTar configuration:')

#print(f'Token: {token}')

#########################################################

Zeitstempel = time.strftime("%d-%m-%Y")

url= URL

Response = requests.get(url, headers={ 'Authorization': 'Bearer ' +token+ ''})

#Speichert JSON File ab 
Data = Response.json()
with open('Data from '+Zeitstempel+'.json', 'w') as outfile:
        json.dump(Data, outfile)
     
#Printet JSON auf die Shell
#print(json.dumps(Data, indent = 4, sort_keys = True))

parse = json.dumps(Data)

pythonObj1 = json.loads(parse)

file = pythonObj1['data']
print(file)

parse1 = json.dumps(file)

#print (parse[27:2634])

# parse json file
pythonObj = json.loads(parse1)

#actual parsing
#start
print ("VON")
start = pythonObj[0]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end = pythonObj[0]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Time for SQL Database

Date = str (
    datetime.datetime.fromtimestamp(
        int(start)/1000
    ).strftime('%d.%m.%Y')
    )

Time = str (
    datetime.datetime.fromtimestamp(
        int(start)/1000
    ).strftime('%H:%M')
    )



#Preis pro kWh
#print ("The Price is")
#price = pythonObj[0]["marketprice"]
#print(float (price)/1000, ("Eur/kWh"))

currency = pythonObj[0]["unit"]
price = pythonObj[0]["marketprice"]
print(float (price), (currency))

Price = float(price)

#MySQL

import mysql.connector

mydb = mysql.connector.connect(
  host=HOST,
  user=USER,
  passwd=PASSWD,
  database=DB,
)

mycursor = mydb.cursor()

sql = "INSERT INTO aWATTar (DATE, TIME, PRICE) VALUES (%s, %s, %s)"
val = (Date, Time, Price)
mycursor.execute(sql, val)

###################################################################

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

#GPIO 17
channel = 22
GPIO.setmode(GPIO.BCM)  
# GPIO 17 (Channel 11)
GPIO.setup(channel, GPIO.OUT)

channel_is_on = GPIO.input(channel)

print (channel_is_on)

sql1 = "INSERT INTO GPIO (DATE, TIME, GPIO) VALUES (%s, %s, %s)"
val1 = (Date, Time, channel_is_on)
mycursor.execute(sql1, val1)

############################################

#GPIO 27
channel2 = 27
GPIO.setmode(GPIO.BCM)  
# GPIO 17 (Channel 11)
GPIO.setup(channel2, GPIO.OUT)

channel_is_on2 = GPIO.input(channel2)

print (channel_is_on2)

sql2 = "INSERT INTO GPIO2 (DATE, TIME, GPIO2) VALUES (%s, %s, %s)"
val2 = (Date, Time, channel_is_on2)
mycursor.execute(sql2, val2)

###########################################

#GPIO 22
channel3 = 17
GPIO.setmode(GPIO.BCM)  
# GPIO 17 (Channel 11)
GPIO.setup(channel3, GPIO.OUT)

channel_is_on3 = GPIO.input(channel3)

print (channel_is_on3)

sql3 = "INSERT INTO GPIO3 (DATE, TIME, GPIO3) VALUES (%s, %s, %s)"
val3 = (Date, Time, channel_is_on3)
mycursor.execute(sql3, val3)

##########################################

#GPIO 26
channel4 = 4
GPIO.setmode(GPIO.BCM)  
# GPIO 17 (Channel 11)
GPIO.setup(channel4, GPIO.OUT)

channel_is_on4 = GPIO.input(channel4)

print (channel_is_on4)

sql4 = "INSERT INTO GPIO4 (DATE, TIME, GPIO4) VALUES (%s, %s, %s)"
val4 = (Date, Time, channel_is_on4)
mycursor.execute(sql4, val4)

mydb.commit()

print(mycursor.rowcount, "record inserted.")