## Setting up the Pi for Plate Scaning

#### Step 1: Installing and setting up Python 3
The program runs using python 3

```bash
$ sudo apt-get update
$ sudo apt-get install python3
```

Note:
This step should install pip3 which is the package manager for python3
but if it doesn't run this command to install it:
```bash
sudo apt-get install python3-pip
```

#### Step 2: Installing Wia python module

To use the Wia python API we need to install it's modules. To do this run this
command:
```bash
sudo pip3 install wia
```

#### Step 3: Setting up the project script
When you have the platescanner.py script downloaded, put it into a new directory called Project.
In the Project directory created a new directory called images this is where the images taken will
be stored. In the Project directory you should have platescanner.py and the images dirctory.

You will need to edit some of the code for the project to work. In Wia.io in the space we have 
created go to the devices tab, select DaemonPi, go to the Configuration tab and copy the **device
secret key**

In the platescanner.py script you will need to add the device secret key. On the 14th line add the
device secret key so that the code looks like this:

```python
wia.access_token = "d_sk_74u2KZL9LXZldmpxHaHraGTr"
```

#### Step 4: Setting up the camera
Use [this tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4)
 to set up the camera


#### Step 5: Running the script
Now everything should work!

In the linux terminal navigate into the Project directory using the **cd** command.
Run the command:

```bash
python3 platescanner.py
```

This should run the script, take an image and publish it to Wia.

