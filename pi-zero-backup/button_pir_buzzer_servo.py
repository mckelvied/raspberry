from gpiozero import MotionSensor
from gpiozero import Servo

pir = MotionSensor(4)
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
servo_gpio=18
servo = Servo(servo_gpio,min_pulse_width=minPW,max_pulse_width=maxPW)

while True:
    pir.wait_for_motion()
    print("You moved!!")
    servo.max()   
 
    pir.wait_for_no_motion()
    print("No motion")
    servo.min()

