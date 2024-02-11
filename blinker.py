from gpiozero import LED
from time import sleep

led = LED(17)

c = True
while True:
    fh = open('ins.txt','r',encoding='utf-8')
    inst = fh.readline()
    if(inst=='on'):
        led.on()
    elif (inst =='off'):
         led.off()
    elif(inst=='blink'):
        if c:
            led.off()
        else:
            led.on()
        c=not c
    sleep(.1)
    fh.close()