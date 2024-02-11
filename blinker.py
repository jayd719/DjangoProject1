print(str(bin(2)))
from gpiozero import LED
from time import sleep

l1= LED(17)



LEDS =[l1]


c = True
while True:
    fh = open('ins.txt','r',encoding='utf-8')
    inst = fh.readline()
    if(inst=='on'):
        LEDS[0].on()
       
    elif (inst =='off'):
          LEDS[0].off()
        
    elif(inst=='blink'):
        if c:
            l1.on()
        else:
            l1.off()
        c=not c
    
   

    sleep(.1)
    fh.close()