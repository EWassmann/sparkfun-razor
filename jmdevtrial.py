from cmath import pi
import time
import numpy as np
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

mpu = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None, 
    bus=8,
    gfs=GFS_1000, 
    afs=AFS_8G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)

mpu.calibrate()
mpu.configure() # Apply the settings to the registers.
magScale = mpu.magScale # Get magnetometer soft iron distortion
print(magScale)
mbias = mpu.mbias # Get magnetometer hard iron distortion
print(mbias)
print("magscale = ", magScale)
print("mbias = ", mbias)
while True:


    #print("|.....MPU9250 in 0x68 Address.....|")
    #print("Accelerometer", mpu.readAccelerometerMaster())
   # print("Gyroscope", mpu.readGyroscopeMaster())
    magreadings = mpu.readMagnetometerMaster()
    print(magreadings)
    
    #head = np.arctan2(magreadings[2],magreadings[1])*(180/pi)
    #print("heading = ", head)
    #print("Magnetometer", mpu.readMagnetometerMaster())
    #print("Temperature", mpu.readTemperatureMaster())
    print("\n")

    time.sleep(1)
