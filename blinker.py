print(str(bin(2)))
from gpiozero import LED
from time import sleep

l1= LED(17)
l2= LED(22)
l3= LED(27)


LEDS =[l1,l2,l3]


c = True
i=0
while True:
    fh = open('ins.txt','r',encoding='utf-8')
    inst = fh.readline()
    if(inst=='on'):
        LEDS[0].on()
        LEDS[1].on()
        LEDS[2].on()
       
    elif (inst =='off'):
          LEDS[0].off()
          LEDS[1].off()
          LEDS[2].off()
        
    elif(inst=='blink'):
        if c:
            LEDS[i].on()
        else:
            LEDS[i].on()
        c=not c
    
   

    sleep(.1)
    fh.close()