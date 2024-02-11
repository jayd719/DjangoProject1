print(str(bin(2)))
from gpiozero import LED
from time import sleep

l1= LED(17)





c = True
while True:
    fh = open('ins.txt','r',encoding='utf-8')
    inst = fh.readline()
    if(inst=='on'):
        l1.on()
       
    elif (inst =='off'):
         l1.off()
        
    elif(inst=='blink'):
        if c:
            l1.on()
        else:
            l1.off()
        c=not c
    
   

    sleep(.1)
    fh.close()