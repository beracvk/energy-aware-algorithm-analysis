import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_results.csv")

algorithms = df["algorithm"].unique()

for algo in algorithms:
    subset = df[df["algorithm"] == algo]

    plt.figure()
    plt.plot(subset["n"], subset["time_sec"], marker="o")
    plt.title(f"{algo} - Time vs Input Size")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.show()

    plt.figure()
    plt.plot(subset["n"], subset["cpu_time"], marker="o")
    plt.title(f"{algo} - Energy (CPU Time) vs Input Size")
    plt.xlabel("Input Size (n)")
    plt.ylabel("CPU Time (proxy for energy)")
    plt.show()
