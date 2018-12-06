# WIT-CMU-Project
A collaboration by WIT and CMU

## The Team
### Wei Kit Wong WIT ｜ Joseph Rodrigues CMU ｜ Daemon Macklin WIT ｜ Yu Zhang CMU

## ALPR
For our project we are using Joseph's idea to do an automatic license plate recognition system.

## Raspberry pi
We are using a [Raspberry pi](https://www.raspberrypi.org/) with the picamera module to take the images. The images are taken automatically by using
a [ST_00081](http://simplytronics.com/products/ST-00081#Technical_Details) PIR sensor that when triggered by movement will take an image.
This image is then published to a flow on Wia.io

## Wia.io
[Wia.io](https://www.wia.io/) is an iot platform that allows users to connect devices, upload data and do all sorts of things.
For this porject the main attraction of Wia is the [Amazon Rekognition](https://aws.amazon.com/rekognition/)
service that will take in images and output any text that is recognized. Wia also allows us to run
basic Javascript functions as well as send data to our own API.

## API
We have created an [API](https://github.com/andyAndyA/license-plate-reader-api) that will take in
the recognized text from the image via Wia.io and first do some processing using regular expressions
that will filter out any unwanted text and leave the license plates. The API will then be able to search 
though a [Mlabs](https://mlab.com/) database to find the plates and then send a response back to
Wia.io which will notify the user if any action is needed.   
