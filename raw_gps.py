import serial
import pynmea2

serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
f = open("raw_gps.txt", "w")

while True:
    str = serialPort.readline()
    print str
    f.write(str)
    f.flush() 
    
f.close()
