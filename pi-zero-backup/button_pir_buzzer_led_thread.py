from gpiozero import MotionSensor
from gpiozero import Buzzer
from gpiozero import Button
from gpiozero import LED
from time import sleep
from threading import Thread


pir = MotionSensor(4)
led = LED(13)
buzzer = Buzzer(17)
button = Button(21)
flashing_alarm = False


def thread_function():
    while True:
        if flashing_alarm:
            print("FLASH ON")
            buzzer.on()
            led.on()
            sleep(0.5)
            print("FLASH OFF")
            buzzer.off()
            led.off()
            sleep(0.5)
        else:  
            sleep(0.1)

t = Thread(target = thread_function, args =())
t.start()


while True:
    pir.wait_for_motion()
    print("You moved, ALARM ACTIVATED!!")
    flashing_alarm = True
    button.wait_for_press()
    print("Button press, ALARM DEACTIVATED")
    flashing_alarm = False
