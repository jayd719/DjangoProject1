
import qrcode 
img = qrcode.make('http://10.10.105.250:8080/controller/')
img.save("output.png")
