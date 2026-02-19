import smbus


class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose=True):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.verbose = verbose
        self.dynamic_range = float(dynamic_range)

        self.pd = 0x00

    def deinit(self):
            self.bus.close()


    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4725 (12 бит)")
            return

        first_byte = ((self.pd & 0x03) << 4) | ((number >> 8) & 0x0F)
        second_byte = number & 0xFF

        self.bus.write_i2c_block_data(self.address, first_byte, [second_byte])

        if self.verbose:
            print(
                f"Число: {number}, отправленные по I2C данные: "
                f"[0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]"
            )

    def set_voltage(self, voltage):
        try:
            v = float(str(voltage).strip().replace(",", "."))
        except Exception:
            print("Вы ввели не число. Попробуйте ещё раз")
            return

        if not (0.0 <= v <= self.dynamic_range):
            print(
                f"Напряжение выходит за динамический диапазон ЦАП "
                f"(0.00 – {self.dynamic_range:.2f} В)"
            )
            v = 0.0

        code = int(round(v / self.dynamic_range * 4095))
        self.set_number(code)
        print(f"Устанавливаем {v:.2f} В (код {code})")


def main():
    dac = MCP4725(dynamic_range=5.1, address=0x61, verbose=True)
    try:
        while True:
            s = input("Введите напряжение в Вольтах: ").strip()
            dac.set_voltage(s)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            dac.set_number(0)
        except Exception:
            pass
        dac.deinit()


if __name__ == "__main__":
    main()