import r2r_dac as r2r
import signal_generator as sg
import time
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
try:
    dac = r2r.R2RDAC()
    t = 0.0
    dt = 1 / sampling_frequency
    
    while True:
        value = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = amplitude * value
        dac.set_voltage(voltage)

        sg.wait_for_sampling_period(sampling_frequency)
        t += dt
finally:
    dac.deinit()