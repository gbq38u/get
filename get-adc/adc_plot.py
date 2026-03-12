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