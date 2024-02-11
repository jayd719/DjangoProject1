from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    fh = open('ins.txt','r',encoding='utf-8')
    if(fh.readline()=='on'):
        led.on()
    else:
        led.off()
    sleep(.3)
    fh.close()