#!/usr/bin/python3
#coding: utf8

import requests
import json
import time
import datetime
import configparser

config = configparser.ConfigParser()
config.read('/home/pi/Python/config.ini')

token = config['awattar']['TOKEN']
URL = config['awattar']['URL']

print('aWATTar configuration:')

print(f'Token: {token}')

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

#Preis pro kWh
#print ("The Price is")
#price = pythonObj[0]["marketprice"]
#print(float (price)/1000, ("Eur/kWh"))

currency = pythonObj[0]["unit"]
price = pythonObj[0]["marketprice"]
print(float (price), (currency))

print ("")

#start
print ("VON")
start1 = pythonObj[1]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start1)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end1 = pythonObj[1]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end1)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price = pythonObj[1]["marketprice"]
#print(float (price)/1000, ("Eur/kWh"))

currency1 = pythonObj[1]["unit"]
price1 = pythonObj[1]["marketprice"]
print(float (price1), (currency1))

print ("")

#start
print ("VON")
start2 = pythonObj[2]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start2)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end2 = pythonObj[2]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end2)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency2 = pythonObj[2]["unit"]
price2 = pythonObj[2]["marketprice"]
print(float (price2), (currency2))

print ("")

#start
print ("VON")
start3 = pythonObj[3]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start3)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end3 = pythonObj[3]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end3)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price3 = pythonObj[3["marketprice"]
#print(float (price3)/1000, ("Eur/kWh"))

currency3 = pythonObj[3]["unit"]
price3 = pythonObj[3]["marketprice"]
print(float (price3), (currency3))

print ("")

#start
print ("VON")
start4 = pythonObj[4]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start4)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end4 = pythonObj[4]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end4)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price4= pythonObj[4]["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency4 = pythonObj[4]["unit"]
price4 = pythonObj[4]["marketprice"]
print(float (price4), (currency4))

print ("")

#start
print ("VON")
start5 = pythonObj[5]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start5)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end5 = pythonObj[5]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end5)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price5 = pythonObj[5["marketprice"]
#print(float (price5)/1000, ("Eur/kWh"))

currency5 = pythonObj[5]["unit"]
price5 = pythonObj[5]["marketprice"]
print(float (price5), (currency5))

print ("")

#start
print ("VON")
start6 = pythonObj[6]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start6)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end6 = pythonObj[6]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end6)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price6 = pythonObj[6["marketprice"]
#print(float (price6)/1000, ("Eur/kWh"))

currency6 = pythonObj[6]["unit"]
price6 = pythonObj[6]["marketprice"]
print(float (price6), (currency6))

print ("")

#start
print ("VON")
start7 = pythonObj[7]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start7)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end7 = pythonObj[7]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end7)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency7 = pythonObj[7]["unit"]
price7 = pythonObj[7]["marketprice"]
print(float (price7), (currency7))

print ("")

#start
print ("VON")
start8 = pythonObj[8]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start8)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end8= pythonObj[8]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end8)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency8 = pythonObj[8]["unit"]
price8 = pythonObj[8]["marketprice"]
print(float (price8), (currency8))

print ("")

#start
print ("VON")
start9 = pythonObj[9]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start9)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end9 = pythonObj[9]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end9)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency9 = pythonObj[9]["unit"]
price9 = pythonObj[9]["marketprice"]
print(float (price9), (currency9))

print ("")

#start
print ("VON")
start10 = pythonObj[10]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start10)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end10 = pythonObj[10]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end10)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency10 = pythonObj[10]["unit"]
price10 = pythonObj[10]["marketprice"]
print(float (price10), (currency10))

print ("")

#start
print ("VON")
start11 = pythonObj[11]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start11)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end11 = pythonObj[11]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end11)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency11 = pythonObj[11]["unit"]
price11 = pythonObj[11]["marketprice"]
print(float (price11), (currency11))

print ("")

#start
print ("VON")
start12 = pythonObj[12]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start12)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end12 = pythonObj[12]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end12)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency12 = pythonObj[12]["unit"]
price12 = pythonObj[12]["marketprice"]
print(float (price12), (currency12))

print ("")

#start
print ("VON")
start13 = pythonObj[13]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start13)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end13 = pythonObj[13]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end13)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency13 = pythonObj[13]["unit"]
price13 = pythonObj[13]["marketprice"]
print(float (price13), (currency13))

print ("")

#start
print ("VON")
start14 = pythonObj[14]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start14)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end14 = pythonObj[14]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end14)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency14 = pythonObj[14]["unit"]
price14 = pythonObj[14]["marketprice"]
print(float (price14), (currency14))

print ("")

#start
print ("VON")
start15 = pythonObj[15]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start15)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end15 = pythonObj[15]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end15)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency15 = pythonObj[15]["unit"]
price15 = pythonObj[15]["marketprice"]
print(float (price15), (currency15))

print ("")

#start
print ("VON")
start16 = pythonObj[16]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start16)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end16 = pythonObj[16]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end16)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency16 = pythonObj[16]["unit"]
price16 = pythonObj[16]["marketprice"]
print(float (price16), (currency16))

print ("")

#start
print ("VON")
start17 = pythonObj[17]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start17)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end17 = pythonObj[17]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end17)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency17 = pythonObj[17]["unit"]
price17 = pythonObj[17]["marketprice"]
print(float (price17), (currency17))

print ("")

#start
print ("VON")
start18 = pythonObj[18]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start18)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end18 = pythonObj[18]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end18)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency18 = pythonObj[18]["unit"]
price18 = pythonObj[18]["marketprice"]
print(float (price18), (currency18))

print ("")

#start
print ("VON")
start19 = pythonObj[19]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start19)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end19 = pythonObj[19]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end19)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency19 = pythonObj[19]["unit"]
price19 = pythonObj[19]["marketprice"]
print(float (price19), (currency19))

print ("")

#start
print ("VON")
start20 = pythonObj[20]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start20)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end20 = pythonObj[20]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end20)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency20 = pythonObj[20]["unit"]
price20 = pythonObj[20]["marketprice"]
print(float (price20), (currency20))

print ("")

#start
print ("VON")
start21 = pythonObj[21]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start21)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end21 = pythonObj[21]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end21)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency21 = pythonObj[21]["unit"]
price21 = pythonObj[21]["marketprice"]
print(float (price21), (currency21))

print ("")

#start
print ("VON")
start22 = pythonObj[22]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start22)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end22 = pythonObj[22]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end22)/1000
    ).strftime('%d.%m.%Y %H:%M')
)

#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency22 = pythonObj[22]["unit"]
price22 = pythonObj[22]["marketprice"]
print(float (price22), (currency22))

print ("")

#start
print ("VON")
start23 = pythonObj[23]["start_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(start23)/1000
    ).strftime('%d.%m.%Y %H:%M')
)
print ("BIS")
end23 = pythonObj[23]["end_timestamp"]
print(
    datetime.datetime.fromtimestamp(
        int(end23)/1000
    ).strftime('%d.%m.%Y %H:%M')
)


#Preis pro kWh
#print ("The Price is")
#price2 = pythonObj[2["marketprice"]
#print(float (price2)/1000, ("Eur/kWh"))

currency23 = pythonObj[23]["unit"]
price23 = pythonObj[23]["marketprice"]
print(float (price23), (currency23))

#Plotting
from datetime import date
today = date.today()

#print("Current year:", today.year)
#print("Current month:", today.month)
#print("Current day:", today.day)

y = int (datetime.datetime.fromtimestamp(int(start)/1000).strftime('%Y'))
m = int (datetime.datetime.fromtimestamp(int(start)/1000).strftime('%m'))
d = int (datetime.datetime.fromtimestamp(int(start)/1000).strftime('%d'))
h = int (datetime.datetime.fromtimestamp(int(start)/1000).strftime('%H'))

y1 = int (datetime.datetime.fromtimestamp(int(start1)/1000).strftime('%Y'))
m1 = int (datetime.datetime.fromtimestamp(int(start1)/1000).strftime('%m'))
d1 = int (datetime.datetime.fromtimestamp(int(start1)/1000).strftime('%d'))
h1 = int (datetime.datetime.fromtimestamp(int(start1)/1000).strftime('%H'))

y2 = int (datetime.datetime.fromtimestamp(int(start2)/1000).strftime('%Y'))
m2 = int (datetime.datetime.fromtimestamp(int(start2)/1000).strftime('%m'))
d2 = int (datetime.datetime.fromtimestamp(int(start2)/1000).strftime('%d'))
h2 = int (datetime.datetime.fromtimestamp(int(start2)/1000).strftime('%H'))

y3 = int (datetime.datetime.fromtimestamp(int(start3)/1000).strftime('%Y'))
m3 = int(datetime.datetime.fromtimestamp(int(start3)/1000).strftime('%m'))
d3 = int(datetime.datetime.fromtimestamp(int(start3)/1000).strftime('%d'))
h3 = int (datetime.datetime.fromtimestamp(int(start3)/1000).strftime('%H'))

y4 = int (datetime.datetime.fromtimestamp(int(start4)/1000).strftime('%Y'))
m4 = int (datetime.datetime.fromtimestamp(int(start4)/1000).strftime('%m'))
d4 = int (datetime.datetime.fromtimestamp(int(start4)/1000).strftime('%d'))
h4 = int (datetime.datetime.fromtimestamp(int(start4)/1000).strftime('%H'))

y5 = int (datetime.datetime.fromtimestamp(int(start5)/1000).strftime('%Y'))
m5 = int (datetime.datetime.fromtimestamp(int(start5)/1000).strftime('%m'))
d5 = int (datetime.datetime.fromtimestamp(int(start5)/1000).strftime('%d'))
h5 = int (datetime.datetime.fromtimestamp(int(start5)/1000).strftime('%H'))

y6 = int (datetime.datetime.fromtimestamp(int(start6)/1000).strftime('%Y'))
m6 = int (datetime.datetime.fromtimestamp(int(start6)/1000).strftime('%m'))
d6 = int (datetime.datetime.fromtimestamp(int(start6)/1000).strftime('%d'))
h6 = int (datetime.datetime.fromtimestamp(int(start6)/1000).strftime('%H'))

y7 = int (datetime.datetime.fromtimestamp(int(start7)/1000).strftime('%Y'))
m7 = int (datetime.datetime.fromtimestamp(int(start7)/1000).strftime('%m'))
d7 = int (datetime.datetime.fromtimestamp(int(start7)/1000).strftime('%d'))
h7 = int (datetime.datetime.fromtimestamp(int(start7)/1000).strftime('%H'))

y8 = int (datetime.datetime.fromtimestamp(int(start8)/1000).strftime('%Y'))
m8 = int (datetime.datetime.fromtimestamp(int(start8)/1000).strftime('%m'))
d8 = int (datetime.datetime.fromtimestamp(int(start8)/1000).strftime('%d'))
h8 = int (datetime.datetime.fromtimestamp(int(start8)/1000).strftime('%H'))

y9 = int (datetime.datetime.fromtimestamp(int(start9)/1000).strftime('%Y'))
m9 = int (datetime.datetime.fromtimestamp(int(start9)/1000).strftime('%m'))
d9 = int (datetime.datetime.fromtimestamp(int(start9)/1000).strftime('%d'))
h9 = int (datetime.datetime.fromtimestamp(int(start9)/1000).strftime('%H'))

y10 = int (datetime.datetime.fromtimestamp(int(start10)/1000).strftime('%Y'))
m10 = int (datetime.datetime.fromtimestamp(int(start10)/1000).strftime('%m'))
d10 = int (datetime.datetime.fromtimestamp(int(start10)/1000).strftime('%d'))
h10 = int (datetime.datetime.fromtimestamp(int(start10)/1000).strftime('%H'))

y11 = int (datetime.datetime.fromtimestamp(int(start11)/1000).strftime('%Y'))
m11 = int (datetime.datetime.fromtimestamp(int(start11)/1000).strftime('%m'))
d11 = int (datetime.datetime.fromtimestamp(int(start11)/1000).strftime('%d'))
h11 = int (datetime.datetime.fromtimestamp(int(start11)/1000).strftime('%H'))

y12 = int (datetime.datetime.fromtimestamp(int(start12)/1000).strftime('%Y'))
m12 = int (datetime.datetime.fromtimestamp(int(start12)/1000).strftime('%m'))
d12 = int (datetime.datetime.fromtimestamp(int(start12)/1000).strftime('%d'))
h12 = int (datetime.datetime.fromtimestamp(int(start12)/1000).strftime('%H'))

y13 = int (datetime.datetime.fromtimestamp(int(start13)/1000).strftime('%Y'))
m13 = int (datetime.datetime.fromtimestamp(int(start13)/1000).strftime('%m'))
d13 = int (datetime.datetime.fromtimestamp(int(start13)/1000).strftime('%d'))
h13 = int (datetime.datetime.fromtimestamp(int(start13)/1000).strftime('%H'))

y14 = int (datetime.datetime.fromtimestamp(int(start14)/1000).strftime('%Y'))
m14 = int (datetime.datetime.fromtimestamp(int(start14)/1000).strftime('%m'))
d14 = int (datetime.datetime.fromtimestamp(int(start14)/1000).strftime('%d'))
h14 = int (datetime.datetime.fromtimestamp(int(start14)/1000).strftime('%H'))

y15 = int (datetime.datetime.fromtimestamp(int(start15)/1000).strftime('%Y'))
m15 = int (datetime.datetime.fromtimestamp(int(start15)/1000).strftime('%m'))
d15 = int (datetime.datetime.fromtimestamp(int(start15)/1000).strftime('%d'))
h15 = int (datetime.datetime.fromtimestamp(int(start15)/1000).strftime('%H'))

y16 = int (datetime.datetime.fromtimestamp(int(start16)/1000).strftime('%Y'))
m16 = int (datetime.datetime.fromtimestamp(int(start16)/1000).strftime('%m'))
d16 = int (datetime.datetime.fromtimestamp(int(start16)/1000).strftime('%d'))
h16 = int (datetime.datetime.fromtimestamp(int(start16)/1000).strftime('%H'))

y17 = int (datetime.datetime.fromtimestamp(int(start17)/1000).strftime('%Y'))
m17 = int (datetime.datetime.fromtimestamp(int(start17)/1000).strftime('%m'))
d17 = int (datetime.datetime.fromtimestamp(int(start17)/1000).strftime('%d'))
h17 = int (datetime.datetime.fromtimestamp(int(start17)/1000).strftime('%H'))

y18 = int (datetime.datetime.fromtimestamp(int(start18)/1000).strftime('%Y'))
m18 = int (datetime.datetime.fromtimestamp(int(start18)/1000).strftime('%m'))
d18 = int (datetime.datetime.fromtimestamp(int(start18)/1000).strftime('%d'))
h18 = int (datetime.datetime.fromtimestamp(int(start18)/1000).strftime('%H'))

y19 = int (datetime.datetime.fromtimestamp(int(start19)/1000).strftime('%Y'))
m19 = int (datetime.datetime.fromtimestamp(int(start19)/1000).strftime('%m'))
d19 = int (datetime.datetime.fromtimestamp(int(start19)/1000).strftime('%d'))
h19 = int (datetime.datetime.fromtimestamp(int(start19)/1000).strftime('%H'))

y20 = int (datetime.datetime.fromtimestamp(int(start20)/1000).strftime('%Y'))
m20 = int (datetime.datetime.fromtimestamp(int(start20)/1000).strftime('%m'))
d20 = int (datetime.datetime.fromtimestamp(int(start20)/1000).strftime('%d'))
h20 = int (datetime.datetime.fromtimestamp(int(start20)/1000).strftime('%H'))

y21 = int (datetime.datetime.fromtimestamp(int(start21)/1000).strftime('%Y'))
m21 = int (datetime.datetime.fromtimestamp(int(start21)/1000).strftime('%m'))
d21 = int (datetime.datetime.fromtimestamp(int(start21)/1000).strftime('%d'))
h21 = int (datetime.datetime.fromtimestamp(int(start21)/1000).strftime('%H'))

y22 = int (datetime.datetime.fromtimestamp(int(start22)/1000).strftime('%Y'))
m22 = int (datetime.datetime.fromtimestamp(int(start22)/1000).strftime('%m'))
d22 = int (datetime.datetime.fromtimestamp(int(start22)/1000).strftime('%d'))
h22 = int (datetime.datetime.fromtimestamp(int(start22)/1000).strftime('%H'))

y23 = int (datetime.datetime.fromtimestamp(int(start23)/1000).strftime('%Y'))
m23 = int (datetime.datetime.fromtimestamp(int(start23)/1000).strftime('%m'))
d23 = int (datetime.datetime.fromtimestamp(int(start23)/1000).strftime('%d'))
h23 = int (datetime.datetime.fromtimestamp(int(start23)/1000).strftime('%H')) 



x = [datetime.datetime(y, m, d, h),
     datetime.datetime(y1, m1, d1, h1),
     datetime.datetime(y2, m2, d2, h2),
     datetime.datetime(y3, m3, d3, h3),
     datetime.datetime(y4, m4, d4, h4),
     datetime.datetime(y5, m5, d5, h5),
     datetime.datetime(y6, m6, d6, h6),
     datetime.datetime(y7, m7, d7, h7),
     datetime.datetime(y8, m8, d8, h8),
     datetime.datetime(y9, m9, d9, h9),
     datetime.datetime(y10, m10, d10, h10),
     datetime.datetime(y11, m11, d11, h11),
     datetime.datetime(y12, m12, d12, h12),
     datetime.datetime(y13, m13, d13, h13),
     datetime.datetime(y14, m14, d14, h14),
     datetime.datetime(y15, m15, d15, h15),
     datetime.datetime(y16, m16, d16, h16),
     datetime.datetime(y17, m17, d17, h17),
     datetime.datetime(y18, m18, d18, h18),
     datetime.datetime(y19, m19, d19, h19),
     datetime.datetime(y20, m20, d20, h20),
     datetime.datetime(y21, m21, d21, h21),
     datetime.datetime(y22, m22, d22, h22),
     datetime.datetime(y23, m23, d23, h23)]

import plotly.graph_objects as go
fig = go.Figure(data=[go.Scatter(x=x, y=[float (price),float (price1), float (price2), float (price3), float (price4), float (price5),
                                         float (price6), float (price7), float (price8), float (price9), float (price10), float (price11),
                                         float (price12), float (price13), float (price14), float (price15), float (price16), float (price17),
                                         float (price18), float (price19), float (price20), float (price21), float (price22), float (price23)])])


fig.update_layout(
    title="aWATTar from "+Zeitstempel,
    xaxis_title="Time",
    yaxis_title="EUR/MWh",
    xaxis_rangeslider_visible=True
)

import plotly
plotly.offline.plot(fig, filename='aWATTar from '+Zeitstempel+'.html')


# Berechnung des Mittelwertes
from statistics import mean

########################################Laufzeit 4 Stunden##################################################

l = [(float (price)), (float (price1)), (float (price2)), (float (price3))]
l1 = [(float (price1)), (float (price2)), (float (price3)), (float (price4))]
l2 = [(float (price2)), (float (price3)), (float (price4)), (float (price5))]
l3 = [(float (price3)), (float (price4)), (float (price5)), (float (price6))]
l4 = [(float (price4)), (float (price5)), (float (price6)), (float (price7))]
l5 = [(float (price5)), (float (price6)), (float (price7)), (float (price8))]
l6 = [(float (price6)), (float (price7)), (float (price8)), (float (price9))]
l7 = [(float (price7)), (float (price8)), (float (price9)), (float (price10))]
l8 = [(float (price8)), (float (price9)), (float (price10)), (float (price11))]
l9 = [(float (price9)), (float (price10)), (float (price11)), (float (price12))]
l10 = [(float (price10)), (float (price11)), (float (price12)), (float (price13))]
l11 = [(float (price11)), (float (price12)), (float (price13)), (float (price14))]
l12 = [(float (price12)), (float (price13)), (float (price14)), (float (price15))]
l13 = [(float (price13)), (float (price14)), (float (price15)), (float (price16))]
l14 = [(float (price14)), (float (price15)), (float (price16)), (float (price17))]
l15 = [(float (price15)), (float (price16)), (float (price17)), (float (price18))]
l16 = [(float (price16)), (float (price17)), (float (price18)), (float (price19))]
l17 = [(float (price17)), (float (price18)), (float (price19)), (float (price20))]
l18 = [(float (price18)), (float (price19)), (float (price20)), (float (price21))]
l19 = [(float (price19)), (float (price20)), (float (price21)), (float (price22))]
l20 = [(float (price20)), (float (price21)), (float (price22)), (float (price23))]

#Durchschnitt-Berechnung
m = float (mean(l))
m1 = float (mean(l1))
m2 = float (mean(l2))
m3 = float (mean(l3))
m4 = float (mean(l4))
m5 = float (mean(l5))
m6 = float (mean(l6))
m7 = float (mean(l7))
m8 = float (mean(l8))
m9 = float (mean(l9))
m10 = float (mean(l10))
m11 = float (mean(l11))
m12 = float (mean(l12))
m13 = float (mean(l13))
m14 = float (mean(l14))
m15 = float (mean(l15))
m16 = float (mean(l16))
m17 = float (mean(l17))
m18 = float (mean(l18))
m19 = float (mean(l19))
m20 = float (mean(l20))

print ("")

#Dict für das Auslesen der min() Variable

var = {m:'A', m1:'B', m2:'C', m3:'D', m4:'E', m5:'F', m6:'G', m7:'H', m8:'I', m9:'J', m10:'K', m11:'L', m12:'M', m13:'N', m14:'O', m15:'P', m16:'Q', m17:'R', m18:'S', m19:'T', m20:'U'}

print (var.get(min(var)))

print ("")

if (var.get(min(var))) == 'A':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h)
    job.minute.on(15)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h4)
    job1.minute.on(1)
    cron.write()
    
    
elif (var.get(min(var))) == 'B':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start1)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h1)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h5)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'C':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start2)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h2)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h6)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'D':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start3)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h3)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h7)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'E':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start4)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h4)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h8)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'F':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start5)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h5)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h9)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'G':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start6)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h6)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h10)
    job1.minute.on(1)
    cron.write()


elif (var.get(min(var))) == 'H':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start7)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h7)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h11)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'I':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start8)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h8)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h12)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'J':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start9)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h9)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h13)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'K':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start10)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h10)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h14)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'L':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start11)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h11)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h15)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'M':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start12)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h12)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h16)
    job1.minute.on(1)
    cron.write()


elif (var.get(min(var))) == 'N':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start13)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h13)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h17)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'O':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start14)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h14)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h18)
    job1.minute.on(1)
    cron.write()


elif (var.get(min(var))) == 'P':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start15)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h15)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h19)
    job1.minute.on(1)
    cron.write()


elif (var.get(min(var))) == 'Q':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start16)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h16)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h20)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'R':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start17)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h17)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h21)
    job1.minute.on(1)
    cron.write()


elif (var.get(min(var))) == 'S':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start18)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h18)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h22)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'T':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start19)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h19)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h23)
    job1.minute.on(1)
    cron.write()

    
elif (var.get(min(var))) == 'U':
    
    print("Optimaler Startzeitpunkt ist:")
    print(
    datetime.datetime.fromtimestamp(
        int(start20)/1000
    ).strftime('%d.%m.%Y %H:%M')
    )
    print ("mit dem Durchschnitspreis von:")
    print (min(var))
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    job = cron.new(command='/home/pi/Python/19E.sh', comment='last3')
    job.hour.on(h20)
    job.minute.on(0)
    cron.write()
    
    job1 = cron.new(command='/home/pi/Python/19D.sh', comment='last3e')
    job1.hour.on(h23+1)
    job1.minute.on(1)
    cron.write()
