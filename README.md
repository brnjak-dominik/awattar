# awattar
awattar load management

User should be "pi"
Put the whole content in a folder named "Python" in the folder "pi"
Path should look like "/home/pi/Python/all the files and folders" 

Before Start your Raspberry Pi should have installed:

- SSH/SFTP
- XRDP
- MySQL Database with PHP MyAdmin 
- Webmin 

Create a Database called "aWATTar" with user "awattar" and passwd "awattar" 
Run the Script CREATE TABLE - on http://localhost/phpmyadmin you can log in

There should be 5 Tables
- aWATTar
- GPIO
- GPIO2
- GPIO3
- GPIO4

With pip or pip3 you should download
(in my case for Python 3+)
- MySQL Connector for Python
- TKINTER for Python
- ttkthemes for Python
- JSON for Python
- requests for Python
- Cronatab for Python
- Matplotlib for Python
- Plotly for Python
- SMTP Lib (optional)

Make ALL the scripts in the folder executable with "chmod +x example.py" in the command line

with the comand "crontab -e" you open the schedeuler
copy the lines from "CRONTAB INPUT" and paste them there
ctrl + o then ENTER and then ctrl+x to EXIT 

In the file "config.ini" you can input your awattar API Token and MySQL credentials (in case you want to change them)

in "/home/pi/Python/UI" is a file "aWATTarAPP.py" that starts the actual User Interface

In case I forgot something - the IDE is going to tell you!
The Project is still IN PROGRESS! 
So far it is working well, but don't be mad, if there are some bugs ;)
