'''
# Copyright 2022 © Centre Interdisciplinaire de développement en Cartographie des Océans (CIDCO), Tous droits réservés
@Jacob Bellavance

'''
#serialPort = open("/dev/ttyUSB0", "w")
import sys
import serial
import os
import time

if (len(sys.argv) < 1):
	print "Use : python3 bridgePump.py <PORT>\nEg: python2 bridgePump.py COM1 "
	sys.exit(0)
else: 
	portName = sys.argv[1]
	
#Open port	
serialPort = serial.Serial(portName, 19200, timeout=1)	
#Infinite loop
while(1):
	#Verify if manually asked to return to port
	#send "gpio read" command
	serialPort.write("gpio read 0"+"\r")
	if (serialPort.read() == 1) :
		activatePump()
		returnToPort()
		
		
	if	


