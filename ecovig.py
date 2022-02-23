import serial
from time import sleep

serial_port = "/dev/tty.e-CoVig"

with serial.Serial(serial_port) as s:
    while True:
        line = ""
        while not line.endswith("}"):
            line += str(s.read(), "ascii")
        print(line)
        sleep(0.1)
