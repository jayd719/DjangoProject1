from django.shortcuts import render
from gpiozero import LED

def controller(requests):
   
    led = LED(17)
    if requests.method == 'POST':
        if requests.POST.get("turnOFF") == "turnOFF":
            led.off()
        

        if requests.POST.get("turnON") == "turnON":
            led.on()
   


    return render(requests,'controller/controller.html')
