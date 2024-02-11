print(str(bin(2)))
from gpiozero import LED
from time import sleep

l1= LED(17)
l2= LED(22)
l3= LED(27)


LEDS =[l1,l2,l3]

def ON():
    i =0
    for each in LEDS:
        LEDS[i].on()
        i+=1


def countdown(t):
    while(t>0):
        i =0
        for ch in str(bin(t))[:2]:
            if ch=='1':
                LEDS[i].on()
            else:
                LEDS[i].off()
            i+=1
        sleep(1)
        print(bin(t))
        t=t-1

c = True
i=0
while True:
    fh = open('ins.txt','r',encoding='utf-8')
    inst = fh.readline()
    if(inst=='on'):
        ON()
       
    elif (inst =='off'):
          LEDS[0].off()
          LEDS[1].off()
          LEDS[2].off()
        
    elif(inst=='blink'):
        if c:
            LEDS[0].off()
            LEDS[1].on()
            LEDS[2].off()
        else:
            LEDS[1].off()
            LEDS[0].on()
            LEDS[2].on()
        c=not c

    elif(inst == 'count'):
        fh.close()
        fh=open('ins.txt','w',encoding='utf-8')
        countdown(9)
        fh.write('on')

    
   

    sleep(.1)
    fh.close()