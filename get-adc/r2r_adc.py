import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.compare_time = compare_time
        self.verbose = verbose

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def close(self):
        self.number_to_dac(0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        if not (0 <= number <= 255):
            raise ValueError("диапазон 0..255")

        bits = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bits)

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            comp_value = GPIO.input(self.comp_gpio)

            if self.verbose:
                print(f"number = {number}, comp = {comp_value}")

            if comp_value == 1:
                return number

        return 255

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        voltage = number / 255 * self.dynamic_range
        return voltage
    






    def successive_approximation_adc(self):
        value = 0

        for bit in range(7, -1, -1):
            test_value = value + (1 << bit)

            self.number_to_dac(test_value)
            time.sleep(self.compare_time)

            comp_value = GPIO.input(self.comp_gpio)

            if comp_value == 0:
                value = test_value

        return value
    def get_sar_voltage(self):
        number = self.successive_approximation_adc()
        voltage = number / 255 * self.dynamic_range
        return voltage







if __name__ == "__main__":
    try:
        adc = R2R_ADC(dynamic_range=3.3)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            time.sleep(0.1)

    finally:
        adc.close()

