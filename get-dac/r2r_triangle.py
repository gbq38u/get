import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 2.0              
signal_frequency = 10        
sampling_frequency = 1000    


dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3          


dac = None
try:
    dac = r2r.R2R_DAC(dac_bits, dynamic_range)

    t = 0.0
    dt = 1 / sampling_frequency

    while True:

        value = sg.get_triangle_wave_amplitude(signal_frequency, t)

        voltage = amplitude * value

        dac.set_voltage(voltage)

        sg.wait_for_sampling_period(sampling_frequency)
        t += dt

finally:
    if dac is not None:
        dac.deinit()