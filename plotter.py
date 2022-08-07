"""
This program below reads data from a sensor till five values and then it writes into a text file. Please pay attention to the range and how to deal with the last element
"""

import serial
import time
import matplotlib.pyplot as plt
import sys
from datetime import datetime

now = datetime.now

#ser = serial.Serial('/dev/cu.usbmodem144401',115200) # This is mac port for windows it will be like COM1
ser = serial.Serial('/dev/cu.usbserial-D30DPYCQ',115200) # This is mac port for windows it will be like COM1

data =[]
count=1
while count <= 15:
    line = ser.readline()  # read a byte
   # print(line)
    string = line.decode()
   # print(string)
    if ('BME' not in string) & ('Setting' not in string) & ('Loop Temp' not in string) & ('=====' not in string):
        print(string)
        string = string.replace('-', ' ')
        string = string.strip()
        string = string.split()

        floats = [float(x) for x in string]
        if (len(floats) > 0):
            data.append(floats)
            count = count + 1


ser.close() # close the connection
print("lendata", len(data))
for i in range(0,len(data)):
  print(i,data[i])

#print(sys.argv)
plotfile = "ria-2"
#with open(sys.argv[1]+".txt", "w") as output:

with open(plotfile + ".txt", "w") as output:
  for i in range(0,len(data)):
    if i != len(data)-1:
      output.write(str(data[i]))
      output.write(",")
      print("writing record", i, data[i])
    else:
      output.write(str(data[4]))
output.close()
plt.plot(data,'r-')
plt.xlabel('Time: in tens of seconds')
plt.ylabel('Gas Reading')
plt.title('BME680 Gas Sensor' + plotfile)
plt.savefig('BME680 Gas Sensor readings' + " " + plotfile+".png")
plt.show()