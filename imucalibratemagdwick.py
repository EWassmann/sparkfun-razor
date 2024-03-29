import os
import sys
import time
import smbus
import numpy as np

from imusensor.MPU9250 import MPU9250
b = 0
address = 0x68
bus = smbus.SMBus(8)
imu = MPU9250.MPU9250(bus, address)
imu.begin()
imu.caliberateGyro()
print("Gyro calibration sucessful")
imu.caliberateAccelerometer()
print ("Acceleration calib successful")
imu.caliberateMagApprox()
print ("Mag calib successful")

accelscale = imu.Accels
accelBias = imu.AccelBias
gyroBias = imu.GyroBias
mags = imu.Mags 
magBias = imu.MagBias

imu.saveCalibDataToFile("/home/gilblankenship/Projects/PythonCode/calib.json")
print ("calib data saved")
b = 1
if b == 1:
	imu.loadCalibDataFromFile("/home/gilblankenship/Projects/PythonCode/calib.json")
	if np.array_equal(accelscale, imu.Accels) & np.array_equal(accelBias, imu.AccelBias) & \
		np.array_equal(mags, imu.Mags) & np.array_equal(magBias, imu.MagBias) & \
		np.array_equal(gyroBias, imu.GyroBias):
		print ("calib loaded properly")
