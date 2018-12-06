#Daemon-Macklin
import time
import RPi.GPIO as io
import plateScanner as ps


io.setmode(io.BCM)

# Using pin 18 on Pi GPIO
pir_pin = 18
io.setup(pir_pin, io.IN)

# Continusly Loop checking input pin status
count = 0
while 1:

    # If the input status is 1
    if io.input(pir_pin):

        # The sensor is returning high and something was detected
        print("Detected")

        # Call start method in the plate scanner script to capture and
        # upload image and then sleep for 10 seconds
        ps.start()
        time.sleep(10)

    # If the input status is 0
    else:

        # The sensor is returning low and nothing has been detected
        print("Not")

    # Print/increment count
    print(count)
    count +=1

    # Wait for one second
    time.sleep(1)
