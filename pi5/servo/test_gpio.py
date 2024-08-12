from gpiozero import Servo
from time import sleep

servo = Servo(18)

while True:
    #:sleep(5)
    print("min")
    servo.min()
    sleep(2)
    print("mid")
    servo.mid()
    sleep(2)
    print("max")
    servo.max()
    sleep(2)
