
import qrcode 
img = qrcode.make('http://10.84.34.144:8000/')
img.save("output.png")
