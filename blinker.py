from gpiozero import LED
from time import sleep



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
       

def allOff():
    for led in LEDS:
        led.off()
def allOn():
    for led in LEDS:
        led.off()

c = True
while True:
    fh = open('ins.txt','r',encoding='utf-8')
    inst = fh.readline()
    if(inst=='on'):
        allOn()
    elif (inst =='off'):
         allOff()
    elif(inst=='blink'):
        if c:
            allOff()
        else:
            allOn()
        c=not c
    
    elif(inst=='count-binary'):
        fh.close()
        fh= open('ins.txt','w',encoding='utf-8')
        countdown(9)
        fh.write('on')
        fh.close()
    
    elif(inst=='hold'):
        allOn()
        sleep(5)
        allOff()




    sleep(.1)
    fh.close()