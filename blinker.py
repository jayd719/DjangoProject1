print(str(bin(2)))
from gpiozero import LED
from time import sleep

l1= LED(17)



LEDS =[l1]


c = True
i=0
while True:
    fh = open('ins.txt','r',encoding='utf-8')
    inst = fh.readline()
    if(inst=='on'):
        LEDS[i].on()
       
    elif (inst =='off'):
          LEDS[i].off()
        
    elif(inst=='blink'):
        if c:
            LEDS[i].on()
        else:
            LEDS[i].on()
        c=not c
    
   

    sleep(.1)
    fh.close()