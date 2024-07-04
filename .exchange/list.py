


# pip install pyserial
import serial
import serial.tools.list_ports
  
plist = list(serial.tools.list_ports.comports())
  
if len(plist) <= 0: 
    print ("The Serial port can't find!")
else:
    plist_0 =list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName,9600,timeout = 60)
    #print ("check which port was really used >",serialFd.name)

    for i in plist:
        print(i)

    print("x5dRRamSUfE6payDGfTC")        