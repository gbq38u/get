from matplotlib import pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.title("Voltage vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.xlim(0, max(time) if time else 1)
    plt.ylim(0, max_voltage)
    plt.grid(True)
    plt.show()







def plot_sampling_period_hist(time):
    sampling_periods = []

    for i in range(1, len(time)):
        sampling_periods.append(time[i] - time[i-1])

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)

    plt.title("Sampling period distribution")
    plt.xlabel("Sampling period (s)")
    plt.ylabel("Number of measurements")

    plt.xlim(0, max(sampling_periods))

    plt.grid(True)
    plt.show()