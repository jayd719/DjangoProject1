print(str(bin(2)))
from gpiozero import LED
from time import sleep

l1= LED(17)
# l2 =LED(27)
# l3 =LED(22)

LEDS=[l1]


def countdown(time):
    while(time>=0):
        i = 0
        for ch in str(bin(time)[2:]):
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
        l1.on()
        allOn()
    elif (inst =='off'):
         l1.off()
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
        fh.close()
        allOn()
        sleep(5)
        allOff()
        fh= open('ins.txt','w',encoding='utf-8')
        fh.write('on')
        fh.close()

    sleep(.1)
    fh.close()