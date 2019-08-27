
from evdev import *
import RPi.GPIO as GPIO

gamepad = InputDevice('/dev/input/event0')

aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308

up = 17
down = 17
left = 16
right = 16

start = 316
select = 315

lTrig = 310
rTrig = 311

lsticku = 1
lstickd = 1
lstickr = 0
lstickl = 0

rsticku = 5
rstickd = 5
rstickr = 2
rstickl = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

print(gamepad)

for event in gamepad.read_loop():


    if event.type == ecodes.EV_ABS:
        if event.value == 1:
            if event.code == down:
                GPIO.output(20,True)
                GPIO.output(26,True)
                print("down")
            elif event.code == right:
                print("right")
                GPIO.output(16,True)
                GPIO.output(26,True)

        elif event.value == -1:
            if event.code == up:
                GPIO.output(16,True)
                GPIO.output(19,True)
                print("up")
            elif event.code == left:
                print("left")
                GPIO.output(19,True)
                GPIO.output(20,True)
        elif event.value == 0:
                GPIO.output(16,False)
                GPIO.output(19,False)
                GPIO.output(20,False)
                GPIO.output(26,False)
