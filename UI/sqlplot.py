#!/usr/bin/python3
#coding: utf8

from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

db_connection_str = 'mysql+pymysql://awattar:awattar@localhost/aWATTar'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM aWATTar', con=db_connection)
df1 = pd.read_sql('SELECT * FROM GPIO', con=db_connection)



print (df)

#fig, ax = plt.subplots()
ax = plt.gca()
ax.set_title('Preisentwicklung VS Verbraucherzeiten', fontsize=23)

df1.plot(secondary_y=True, kind='line',x='DATE',y='GPIO', color='red', label="Verbraucher", ax=ax)
df.plot(kind='line',x='DATE',y='PRICE', color='blue', label="Preis", ax=ax)

import numpy as np
plt.yticks(np.arange(0, 3))

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())


ax.minorticks_on()
ax.set_axisbelow(True)
ax.grid(which="major", linestyle='-', linewidth='1', color='#999999')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='#999999')

ax.set_xlabel('Datum', fontsize=15)
ax.set_ylabel('MWh', fontsize=15)
ax.legend(loc='best')
plt.legend(loc="upper left")

db_connection.dispose()

plt.draw()

plt.show()

