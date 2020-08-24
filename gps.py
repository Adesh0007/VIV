#CODE FOR REAL TIME GPS TRACKING.
import pynmea2       #MODULE FOR GPS( "pip install pynmea2" to install pynmea2 in windows")
import serial
import time
import string




def gps():
    while True:
		port="/dev/ttyAMA0"
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)
		dataout = pynmea2.NMEAStreamReader()
		newdata=ser.readline()

		if newdata[0:6] == "$GPRMC":
			newmsg=pynmea2.parse(newdata)
			lat=newmsg.latitude
			lng=newmsg.longitude
			gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
			print(gps)1
