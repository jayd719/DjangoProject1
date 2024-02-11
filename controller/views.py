from django.shortcuts import render
from gpiozero import LED

def controller(requests):
   
    
    if requests.method == 'POST':
        led = LED(17)
        if requests.POST.get("turnOFF") == "turnOFF":
            led.off()
        

        if requests.POST.get("turnON") == "turnON":
            led.on()
   


    return render(requests,'controller/controller.html')
