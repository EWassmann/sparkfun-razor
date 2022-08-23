######################################################
# Copyright (c) 2020 Maker Portal LLC
# Author: Joshua Hrisko
######################################################
#
# This code reads data from the MPU9250/MPU9265 board
# (MPU6050 - accel/gyro, AK8963 - mag) to verify its
# correct wiring to a Raspberry Pi and the functionality
# of the MPU9250_i2c.py library
#
#
######################################################
#
from cmath import pi
import time
import numpy as np
t0 = time.time()
start_bool = False # boolean for connection
while (time.time()-t0)<5: # wait for 5-sec to connect to IMU
    try:
        from mpu9250_i2c import *
        start_bool = True # True for forthcoming loop
        break 
    except:
        continue
#
#############################
# Strings for Units/Labs
#############################
#
imu_devs   = ["MAGNETOMETER"]
imu_labels = ["x-dir","y-dir","z-dir","heading"]
imu_units  = ["uT","uT","uT","deg"]
#
#############################
# Main Loop to Test IMU
#############################
#
while True:
    if start_bool==False: # make sure the IMU was started
        print("IMU not Started, Check Wiring") # check wiring if error
        break
    ##################################
    # Reading and Printing IMU values
    ##################################
    #
    try:
        ax,ay,az,wx,wy,wz = mpu6050_conv() # read and convert mpu6050 data
        mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
        mx = mx + 30.1025390625
        my = my +  25.634765625
        mz = mz - 24.0966796875
        heading = np.arctan2(my,mx)*(180/pi)
    except:
        continue 
    #
    ##################################
    # Reading and Printing IMU values
    ##################################
    #
    print(50*"-")
    for imu_ii,imu_val in enumerate([mx,my,mz,heading]):
        if imu_ii%4==0:
            print(20*"_"+"\n"+imu_devs[int(imu_ii/4)]) # print sensor header
        #
        ###############
        # Print Data
        ###############
        #
        print("{0}: {1:3.2f} {2}".format(imu_labels[imu_ii%4],imu_val,imu_units[imu_ii]))
        
    time.sleep(1) # wait between prints
    