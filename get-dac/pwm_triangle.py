import wm_dac as wm
import signal_generator as sg
import time


# параметры сигнала
amplitude = 2.0            # В
signal_frequency = 10      # Гц
sampling_frequency = 1000  # Гц

# параметры PWM DAC
pwm_pin = 18               # GPIO с аппаратным PWM
pwm_frequency = 1000       # Гц
dynamic_range = 3.3        # В


dac = None
try:
    dac = wm.WMDAC(pwm_pin, pwm_frequency, dynamic_range)

    t = 0.0
    dt = 1 / sampling_frequency

    while True:
        # 0..1 треугольник
        value = sg.get_triangle_wave_amplitude(signal_frequency, t)

        # перевод в вольты
        voltage = amplitude * value

        # подача на OUT PWM DAC
        dac.set_voltage(voltage)

        sg.wait_for_sampling_period(sampling_frequency)
        t += dt

finally:
    if dac is not None:
        dac.deinit()