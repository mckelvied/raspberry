from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)
while True:
    buzzer.beep()
    sleep(1)
