import time
from mcp3021 import MCP3021
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

voltage_values = []
time_values = []

duration = 3.0
dynamic_range = 5.0

adc = None

try:
    adc = MCP3021(dynamic_range)

    start_time = time.time()

    while time.time() - start_time < duration:
        voltage = adc.get_voltage()
        current_time = time.time() - start_time

        voltage_values.append(voltage)
        time_values.append(current_time)

    plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    plot_sampling_period_hist(time_values)

finally:
    if adc is not None:
        adc.deinit()