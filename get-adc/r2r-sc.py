import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time,plot_sampling_period_hist


voltage_values = []
time_values = []
duration = 3.0

adc = R2R_ADC(dynamic_range=3.3, compare_time=0.0001)

try:
    start_time = time.time()

    while time.time() - start_time < duration:
        current_time = time.time() - start_time
        voltage = adc.get_sc_voltage()

        time_values.append(current_time)
        voltage_values.append(voltage)

    plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)

finally:
    adc.close()