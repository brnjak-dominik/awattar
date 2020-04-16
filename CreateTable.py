#!/usr/bin/python3
#coding: utf8

import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('/home/pi/Python/config.ini')

HOST = config['mysql']['host']
USER = config['mysql']['user']
PASSWD = config['mysql']['passwd']
DB = config['mysql']['db']


mydb = mysql.connector.connect(
  host=HOST,
  user=USER,
  passwd=PASSWD,
  database=DB,
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE aWATTar (id INT AUTO_INCREMENT PRIMARY KEY, DATE VARCHAR(255), TIME VARCHAR(255), PRICE float(25))")

mycursor.execute("CREATE TABLE GPIO (id INT AUTO_INCREMENT PRIMARY KEY, DATE VARCHAR(255), TIME VARCHAR(255), GPIO INT)")

mycursor.execute("CREATE TABLE GPIO2 (id INT AUTO_INCREMENT PRIMARY KEY, DATE VARCHAR(255), TIME VARCHAR(255), GPIO2 INT)")

mycursor.execute("CREATE TABLE GPIO3 (id INT AUTO_INCREMENT PRIMARY KEY, DATE VARCHAR(255), TIME VARCHAR(255), GPIO3 INT)")

mycursor.execute("CREATE TABLE GPIO4 (id INT AUTO_INCREMENT PRIMARY KEY, DATE VARCHAR(255), TIME VARCHAR(255), GPIO4 INT)")
