from gpiozero import MotionSensor
from gpiozero import Buzzer
from gpiozero import Button
from gpiozero import LED
from time import sleep

pir = MotionSensor(4)
led = LED(13)
buzzer = Buzzer(17)
button = Button(21)

while True:
    #button.wait_for_press()
    #print("Pressed")
    pir.wait_for_motion()
    print("You moved, ALARM ACTIVATED!!")
    buzzer.on()
    led.on() 
    button.wait_for_press()
    print("Button press, ALARM DEACTIVATED")
    #pir.wait_for_no_motion()
    #print("No motion")
    buzzer.off()
    led.off()

