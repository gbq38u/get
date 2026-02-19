import wm_dac as wm
import signal_generator as sg
import time
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
dac = None
pwm_pin = 12
pwm_frequancy = 1000
dynamic_range = 3.3
try:
    dac = wm.PWM_DAC(pwm_pin,pwm_frequancy,dynamic_range)
    t = 0.0
    dt = 1 / sampling_frequency
    while True:
        value = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = amplitude * value
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t += dt
finally:
    if dac is not None:
        dac.deinit()