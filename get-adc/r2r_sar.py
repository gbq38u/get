import time
from r2r_adc import R2R_ADC


adc = R2R_ADC(dynamic_range=3.3)

try:
    while True:
        voltage = adc.get_sar_voltage()
        print(f"Voltage: {voltage:.3f} V")
        time.sleep(0.1)

finally:
    adc.close()