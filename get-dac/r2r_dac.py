import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = float(dynamic_range)
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        n = int(number)
        if n < 0:
            n = 0
        if n > 255:
            n = 255

        bits = [int(b) for b in bin(n)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, bits)

        if self.verbose:
            voltage = n / 255 * self.dynamic_range
            print(f"number={n:3d}  bits={''.join(map(str, bits))}  voltage≈{voltage:.3f} V")

    def set_voltage(self, voltage):
        v = float(voltage)

        if not (0.0 <= v <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение вне диапазона 0..{self.dynamic_range:.3f} В, ставим 0")
            self.set_number(0)
            return

        n = int(v / self.dynamic_range * 255)
        self.set_number(n)


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()