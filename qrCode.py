
import qrcode 
img = qrcode.make('http://10.10.105.250:8080/')
img.save("output.png")
