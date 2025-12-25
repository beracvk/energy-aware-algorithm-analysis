import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("emissions.csv")

energy_df = df[["project_name", "energy_consumed"]]

mean_energy = (
    energy_df
    .groupby("project_name")
    .mean()
    .reset_index()
)

mean_energy[["algorithm", "level"]] = (
    mean_energy["project_name"].str.split("-", expand=True)
)


level_order = ["low", "medium", "high"]

for algo in mean_energy["algorithm"].unique():

    algo_data = mean_energy[
        mean_energy["algorithm"] == algo
    ][["level", "energy_consumed"]]


    algo_data["level"] = pd.Categorical(
        algo_data["level"],
        categories=level_order,
        ordered=True
    )
    algo_data = algo_data.sort_values("level")

    # 🔹 TABLO
    print(f"\n{algo} Energy Table (LOW / MEDIUM / HIGH)")
    print(algo_data)

    # 🔹 GRAFİK
    plt.figure()
    plt.plot(
        algo_data["level"],
        algo_data["energy_consumed"],
        marker="o"
    )

    plt.title(f"{algo} Energy Consumption")
    plt.xlabel("Input Size Level")
    plt.ylabel("Energy Consumed (kWh)")
    plt.grid(True)


    filename = f"{algo.lower()}_energy.png"
    plt.savefig(filename, dpi=300)
    plt.show()
