#Daemon-Macklin
from wia import Wia
from picamera import PiCamera
from picamera import PiResolution
from time import sleep
import uuid


#Method to continusly upload captured images to wia 
def start():

    #Starting new Wia class and setting decivce's secret access token
    wia = Wia()
    wia.access_token = "d_sk_oBF5nGQeQk8VvOZvqXzMsUSr"

    #Infinte Loop taking images and uploading them to WIA flow
    while(1):

        #Calling image
        image = capture()

        #Check is the image is null
        if image is not None:

            #If Image is not null try to upload it to WIA flow by
            #publishing it to event named image
            #If the publish fails print the error
            try:
                wia.Event.publish(name = "image",file = image)
            except Exception as e:
                print(e)
        else:

            #If Image is null print error mesage 
            print("Error Capturing Image")

        #Sleep 10 seconds before taking another image
        time.sleep(10)
        

def capture():

    #Starting new PiCamera class and setting resolution of images taken
    camera = PiCamera()
    camera.resolution = (1000,800)

    #Generating a unique filename
    fileName = "images/"+str(uuid.uuid4())+".jpeg"

    #Try to capture an image
    try:

        #Capture a new image with using the variable filename as a name
        camera.capture(fileName)
        print(fileName)

        #Close camera and return the file name
        camera.close()
        return fileName
    except Exception as e:

        #print error and close camera and return null
        print(e)    
        camera.close()
        return None


#Starting program
if __name__ == '__main__':
    start()
