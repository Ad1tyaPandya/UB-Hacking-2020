import serial
import time

BAUD_RATE = 9600
PORT = "COM3"
BYTESIZE = 8
TIMEOUT = 5

serialPort = serial.Serial(port=PORT, baudrate=BAUD_RATE, timeout=TIMEOUT)

for i in range(10):
    data = serialPort.read(1)
    character = data.decode("ASCII")
    print(character)
    if (character == 'b'):
        ohno()
    time.sleep(1)
    
serialPort.close()

def ohno():
    print("There's a fire")
