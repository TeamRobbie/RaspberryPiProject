import serial
from time import sleep

bluetoothSerial = serial.Serial("/dev/rfcomm1", baudrate=9600)

while 1:   
    data=str(bluetoothSerial.readline()).rstrip('\r\n')
    if data=="-1":
        print str(bluetoothSerial.readline()).rstrip('\r\n')
        speed = raw_input("Speed (0-255) = ")
        bluetoothSerial.write(speed);
        print str(bluetoothSerial.readline()).rstrip('\r\n')
        KP = raw_input("KP = ")
        bluetoothSerial.write(KP);
        print str(bluetoothSerial.readline()).rstrip('\r\n')
        KI = raw_input("KI = ")
        bluetoothSerial.write(KI);
        print str(bluetoothSerial.readline()).rstrip('\r\n')
        KD = raw_input("KD = ")
        bluetoothSerial.write(KD);
        print "----------------------------------------"
    else:
        print data
