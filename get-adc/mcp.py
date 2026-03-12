import time
import smbus
from adc_plot import plot_voltage_vs_time

bus = smbus.SMBus(1)
address = 0x4D   

voltage_values = []
time_values = []
duration = 3.0
vref = 3.3

def read_voltage():
    data = bus.read_i2c_block_data(address, 0, 2)
    value = ((data[0] << 8) + data[1]) >> 2
    voltage = value / 1023 * vref
    return voltage


try:
    start_time = time.time()

    while time.time() - start_time < duration:
        voltage = read_voltage()
        current_time = time.time() - start_time

        voltage_values.append(voltage)
        time_values.append(current_time)

finally:
    plot_voltage_vs_time(time_values, voltage_values, vref)