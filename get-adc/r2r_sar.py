import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time

voltage_values = []
time_values = []
duration = 3.0
adc = R2R_ADC(dynamic_range=3.3)

try:
    while True:
        voltage = adc.get_sar_voltage()
        print(f"Voltage: {voltage:.3f} V")
        time.sleep(0.1)

finally:
    adc.close()








#График и гистор=грамма напряжений на входе АЦП ПП


"""import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

voltage_values = []
time_values = []
duration = 3.0

adc = R2R_ADC(dynamic_range=3.3)

try:
    start_time = time.time()

    while time.time() - start_time < duration:
        voltage = adc.get_sar_voltage()
        current_time = time.time() - start_time

        voltage_values.append(voltage)
        time_values.append(current_time)

    plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
    plot_sampling_period_hist(time_values)

finally:
    adc.close()"""