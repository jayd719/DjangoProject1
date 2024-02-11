from gpiozero import LED
from time import sleep

led = LED(17)

LEDS=[LED(17),LED(27),LED(22)]


def countdown(time):
    while(time>=0):
        i = 0
        for ch in str(bin(time)):
            if ch=='1':
                LEDS[i].on()
            else:
                LEDS[i].off()
            i+=1
        
        print(time)
       

 

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
    
    elif(inst=='count-binary'):
        fh.close()
        fh= open('ins.txt','w',encoding='utf-8')
        countdown(9)
        fh.write('on')
        fh.close()



    sleep(.1)
    fh.close()