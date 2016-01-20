import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 11
Motor1B = 12
Motor1E = 13
GPIO.setup(Motor1A,GPIO.OUT)

GPIO.setup(Motor1B,GPIO.OUT)

GPIO.setup(Motor1E,GPIO.OUT)
def clockwise():
    print "Turning motor on Clockwise."
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)

def counterclockwise():
    print "Turning motor on Counterclockwise."
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

def stopmotor():
    print "Stopping motor"
    GPIO.output(Motor1E,GPIO.LOW)

while True:
    cmd = raw_input("Command, q/s/w/e ")
    direction = cmd[0]
    if direction == "q":
        clockwise()
    elif direction == "s":
        stopmotor()
    elif direction == "w":
        counterclockwise()
    elif direction == "e":
        GPIO.cleanup()
        break
