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
            LEDS[0].on()
        else:
            LEDS[0].off()
            LEDS[0].on()
        c=not c
    
   

    sleep(.1)
    fh.close()