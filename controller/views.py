from django.shortcuts import render

def controller(requests):
   
    

    if requests.method == 'POST':
        fh = open('ins.txt','w',encoding='utf-8')
        
        if requests.POST.get("turnOFF") == "turnOFF":
            fh.write('off')
        

        if requests.POST.get("turnON") == "turnON":
            fh.write('on')
        
        if requests.POST.get("blink") == "blink":
            fh.write('blink')
        
        if requests.POST.get("count-binary") == "count-binary":
            fh.write('count')
        
        if requests.POST.get("hold") == "hold":
            fh.write('hold')


   


    return render(requests,'controller/controller.html')
