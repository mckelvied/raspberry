from gpiozero import Buzzer
from gpiozero import Button
from time import sleep

buzzer = Buzzer(17)
#button = Button(2)
button = Button(21)

while True:
    button.wait_for_press()
    print("Pressed")
    buzzer.on()
    button.wait_for_release()
    print("Released")
    buzzer.off()

