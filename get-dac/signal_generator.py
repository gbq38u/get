import numpy as np
import time
def get_sin_wave_amplitude(freq, t):
    return (np.sin(2 * np.pi * freq * t) + 1) / 2
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)

def get_triangle_wave_amplitude(freq, time):
    period = 1.0 / freq
    phase = (time % period) / period

    if phase < 0.5:
        return 2 * phase      
    else:
        return 2 * (1 - phase)  