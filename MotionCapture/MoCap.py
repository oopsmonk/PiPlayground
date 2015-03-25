#!/usr/bin/env python

from bottle import get, run, template, static_file
import os, inspect, json
import time
import math
import mpu6050
from threading import Thread
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

rootPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

class Motion(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.ypr = []
        self.stop = True

    def run(self):
        mpu = mpu6050.MPU6050()
        mpu.dmpInitialize()
        mpu.setDMPEnabled(True)

        # get expected DMP packet size for later comparison
        packetSize = mpu.dmpGetFIFOPacketSize() 
        while True:
            # Get INT_STATUS byte
            mpuIntStatus = mpu.getIntStatus()
          
            if mpuIntStatus >= 2: # check for DMP data ready interrupt (this should happen frequently) 
                # get current FIFO count
                fifoCount = mpu.getFIFOCount()
                
                # check for overflow (this should never happen unless our code is too inefficient)
                if fifoCount == 1024:
                    # reset so we can continue cleanly
                    mpu.resetFIFO()
                    print('FIFO overflow!')
                    
                    
                # wait for correct available data length, should be a VERY short wait
                fifoCount = mpu.getFIFOCount()
                while fifoCount < packetSize:
                    fifoCount = mpu.getFIFOCount()
                
                result = mpu.getFIFOBytes(packetSize)
                q = mpu.dmpGetQuaternion(result)
                g = mpu.dmpGetGravity(q)
                self.ypr = mpu.dmpGetYawPitchRoll(q, g)
                self.ypr['yaw'] = self.ypr['yaw'] * 180 / math.pi
                self.ypr['pitch'] = self.ypr['pitch'] * 180 / math.pi
                self.ypr['roll'] = self.ypr['roll'] * 180 / math.pi
                
                #print(ypr['yaw'] * 180 / math.pi),
                #print(ypr['pitch'] * 180 / math.pi),
                #print(ypr['roll'] * 180 / math.pi)
            
                # track FIFO count here in case there is > 1 packet available
                # (this lets us immediately read more without waiting for an interrupt)        
                fifoCount -= packetSize  
                #print "ypr = ", ypr
                if self.checkStop() == False:
                    print "Thread STOP"
                    break

    def getRPY(self):
        return self.ypr

    def Onstop(self):
        self.stop = False

    def checkStop(self):
        return self.stop

@get('/assets/<filepath:path>')
def assets_file(filepath):
    return static_file(filepath, root=rootPath+'/assets')

@get('/')
def index():
    return template('index')

@get('/websocket', apply=[websocket])
def echo(ws):
    mpu = mpu6050.MPU6050()
    mpu.dmpInitialize()
    mpu.setDMPEnabled(True)

    # get expected DMP packet size for later comparison
    packetSize = mpu.dmpGetFIFOPacketSize() 
    while True:
        # Get INT_STATUS byte
        mpuIntStatus = mpu.getIntStatus()
      
        if mpuIntStatus >= 2: # check for DMP data ready interrupt (this should happen frequently) 
            # get current FIFO count
            fifoCount = mpu.getFIFOCount()
            
            # check for overflow (this should never happen unless our code is too inefficient)
            if fifoCount == 1024:
                # reset so we can continue cleanly
                mpu.resetFIFO()
                print('FIFO overflow!')
                
                
            # wait for correct available data length, should be a VERY short wait
            fifoCount = mpu.getFIFOCount()
            while fifoCount < packetSize:
                fifoCount = mpu.getFIFOCount()
            
            result = mpu.getFIFOBytes(packetSize)
            q = mpu.dmpGetQuaternion(result)
            g = mpu.dmpGetGravity(q)
            ypr = mpu.dmpGetYawPitchRoll(q, g)
            ypr['yaw'] = ypr['yaw'] * 180 / math.pi
            ypr['pitch'] = ypr['pitch'] * 180 / math.pi
            ypr['roll'] = ypr['roll'] * 180 / math.pi
            ws.send(json.dumps(ypr))
            print ypr
            
            #print(ypr['yaw'] * 180 / math.pi),
            #print(ypr['pitch'] * 180 / math.pi),
            #print(ypr['roll'] * 180 / math.pi)
        
            # track FIFO count here in case there is > 1 packet available
            # (this lets us immediately read more without waiting for an interrupt)        
            fifoCount -= packetSize  

    #mp = Motion()
    #mp.start()
    #while True:
        #msg = ws.receive()
        #if msg == 'g':
            #data = mp.getRPY()
            #print "sned ", data 
            #ws.send(json.dumps(data))
        #else: 
            #break

    #mp.Onstop()
    #mp.join()

if __name__ == "__main__":
    #run(host='127.0.0.1', port=8888, server=GeventWebSocketServer)
    run(host='192.168.11.25', port=8888, server=GeventWebSocketServer)

