from __future__ import print_function
from math import atan2, pi
import qwiic_icm20948
import serial
import time
import sys
IMU = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=1)
def runExample():

	# print("\nSparkFun 9DoF ICM-20948 Sensor  Example 1\n")
	# IMU = qwiic_icm20948.QwiicIcm20948()

	# if IMU.connected == False:
	# 	print("The Qwiic ICM20948 device isn't connected to the system. Please check your connection", \
	# 		file=sys.stderr)
	# 	return

	# IMU.begin()

		while True:
		# if IMU.dataReady():
			lne = IMU.readline() # read all axis and temp from sensor, note this also updates all instance variables
			lne1 = lne.strip()
			lne2 = lne1.decode()
			lne3 = lne2.split(",")
			timems = lne3[0]
			accelX = lne3[1]
			accelY = lne3[2]
			accelZ = lne3[3]
			gyroX = lne3[4]
			gyroY = lne3[5]
			gyroZ = lne3[6]
			magX = float(lne3[7])
			magY = float(lne3[8])
			magZ = float(lne3[9])
			head = atan2(magY, magX)* (180/pi)
			print(head)
			time.sleep(.05)
			#print('magx:',magX,'  magy:',magY,'  magz:',magZ) 
			#print('gyrox:',gyroX,'  gyroy',gyroY,'  gyroz:',gyroZ)
			#time.sleep(2)
			# print()
			# print()
	

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		IMU.close()
		sys.exit(0)