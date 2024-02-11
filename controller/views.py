from django.shortcuts import render

def controller(requests):
   
    

    if requests.method == 'POST':
        fh = open('ins.txt','w',encoding='utf-8')
        
        if requests.POST.get("turnOFF") == "turnOFF":
            fh.write('off')
        

        if requests.POST.get("turnON") == "turnON":
            fh.write('on')
           
   


    return render(requests,'controller/controller.html')
