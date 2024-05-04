import RPi.GPIO as gpio
import time
import sys
import TKinter as tk
from sensor import distance
import random

def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)

    gpio.output(12, False)
    while gpio.input(16) == 0:
        nosig = time.time()

    while gpio.input(16) == 1:
        sig = time.time()

    tl = sig - nosig

    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print('improper choice of measurement: in or cm')
        distance = None

    gpio.cleanup()
    return distance

    except:
        distance = 100
        gpio.cleanup()
        return distance

#print(distance('cm'))


def init():
    gpio.setmode(gpio.BOARD)

    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def fwd(tf):
    
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def bwd(tf):

    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def links(tf):

    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def recht(tf):

    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()
    

def key_input(event):
    init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        fwd(sleep_time)
    elif key_press.lower() == 's':
        bwd(sleep_time)
    elif key_press.lower() == 'a':
        links(sleep_time)
    elif key_press.lower() == 'd':
        recht(sleep_time)
    else:
        pass

command = tk.TK()
command.blind('<KeyPress>', key_input)
command.mainloop()


def check_front():
    init()
    dist = distance()

    if dist < 15:
        print('2 Close MuthaTrucka,',dist)
        init()
        bwd(2)
        dist = distance()
        if dist < 15:
            print('2 Close MuthaTrucka,',dist)
            init()
            links(3)
            init()
            bwd(2)
            dist = distance()
            if dist < 15:
                print('2 Close MuthaTrucka,',dist)
                sys.exit()


def autonomy():
    tf = 0.030
    x = random.randrange(0,4)

    if x == 0:
        for y in range(30):
            check_front()
            init()
            forward(tf)
    elif x == 1:
        for y in range(30):
            check_front()
            init()
            links(tf)
    elif x == 2:
        for y in range(30):
            check_front()
            init()
            recht(tf)
    elif x == 3:
        for y in range(30):
            check_front()
            init()
            links(tf)

    for z in range(10):
        autonomy()
    
    
