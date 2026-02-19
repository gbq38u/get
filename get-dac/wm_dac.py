import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = int(gpio_pin)
        self.pwm_frequency = float(pwm_frequency)
        self.dynamic_range = float(dynamic_range)
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial=GPIO.LOW)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)  

    def deinit(self):
        try:
            self.pwm.ChangeDutyCycle(0)
            self.pwm.stop()
        finally:
            GPIO.output(self.gpio_pin, GPIO.LOW)
            GPIO.cleanup()

    def set_voltage(self, voltage):
        v = float(voltage)

        if not (0.0 <= v <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение вне диапазона 0..{self.dynamic_range:.3f} В, ставим 0")
            v = 0.0

        duty = v / self.dynamic_range * 100.0
        if duty < 0.0:
            duty = 0.0
        if duty > 100.0:
            duty = 100.0

        self.pwm.ChangeDutyCycle(duty)

        if self.verbose:
            print(f"voltage={v:.3f} V  duty={duty:.1f}%  freq={self.pwm_frequency:.1f} Hz")


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()