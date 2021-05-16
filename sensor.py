from gpiozero import DistanceSensor
from gpiozero import Servo
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23)
servo = Servo(17)

while True:
    print('Distance: ', sensor.distance * 100)
    if (sensor.distance * 100 < 2):
        servo.min()
        sleep(0.5)
        servo.max()
    sleep(1)