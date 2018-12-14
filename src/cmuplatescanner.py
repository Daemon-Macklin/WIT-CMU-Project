from wia import Wia
from subprocess import call
import os
import time

##While loop to continuously run program
While(1):
    ##Take image using USB Camera
    call(["fswebcam", "--no-banner", "image.jpg"])

    ##Wia Device information
    wia = Wia()
    wia.access_token = "d_sk_Bi6s9KuRIoNg0O2AiPqBOnMj"

    ##Publish Image to WIA
    wia.Event.publish(name = "image",file = open('/home/pi/image.jpg'))
    print("Image published")

    ##Deletes previous picture from RPI memory to conserve space
    path = '/home/pi'
    img_name = 'image.jpg'
    os.remove(path + '/' + img_name)

    ##Add delay between iterations of program taking and broadcasting pictures.
    time.sleep(2.5)
