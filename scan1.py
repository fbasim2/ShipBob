from picamera import PiCamera
from time import sleep

from PIL import Image
import zbarlight

camera = PiCamera()

while True:
#start
    camera.start_preview()
#Camera warmup
    sleep(5)
#Capture Image
    camera.capture('/home/p1/Desktop/q1.png')
#close camera (critical)
    camera.stop_preview()

    file_path = '/home/pi/Desktop/qrtest.png'
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
        
    sleep(5)#wait for pause and see
    codes = zbarlight.scan_codes(['qrcode'], image) 
    print('QR code: %s' % codes)

