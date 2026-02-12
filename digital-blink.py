import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

state = 0
period = 1.0

try:
    while True:
        GPIO.output(led, state)
        state = 1 - state  # 0->1, 1->0
        time.sleep(period)
finally:
    GPIO.output(led, 0)
    GPIO.cleanup()