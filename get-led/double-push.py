import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]


up = 19
down = 26

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(x) for x in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    up_pressed = GPIO.input(up) == 1
    down_pressed = GPIO.input(down) == 1

    if up_pressed and down_pressed:
        num = 255
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    elif up_pressed:
        num = min(255, num + 1)
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    elif down_pressed:
        num = max(0, num - 1)
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    GPIO.output(leds, dec2bin(num))