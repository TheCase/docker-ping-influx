#!/usr/bin/env python

import ping
import time
import os

from influxdb import InfluxDBClient
def influx( addr, meas, value):
   client = InfluxDBClient(os.environ['INFLUXHOST'], os.environ['INFLUXPORT'], os.environ['INFLUXUSER'], os.environ['INFLUXPASS'], os.environ['INFLUXDB'])
   print("{0}, {1}, {2}").format(addr,meas,value)
   if value == None: 
      value = 0
   data = [ 
         {   
           "measurement": str(meas), 
           "tags":  { "address": addr }, 
           "fields": { "value": float(value) }
         }   
   ]   
   client.write_points(data)


def hit(addr,timeout=1,count=1,packet_size=128):
  res = ping.quiet_ping(addr,timeout,count,packet_size) 
  influx(addr, 'lost', res[0])
  influx(addr, 'max',  res[1])
  influx(addr, 'avg',  res[2])

targets = os.environ['TARGETS']
for target in targets.split( ):
   hit(target)
