import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ CSV oku
df = pd.read_csv("emissions.csv")

# 2️⃣ SADECE GEREKLİ OLANLAR
energy_df = df[["project_name", "energy_consumed"]]

# 3️⃣ ORTALAMA (MEAN)
mean_energy = (
    energy_df
    .groupby("project_name")
    .mean()
    .reset_index()
)

# 4️⃣ Algorithm ve level ayır
mean_energy[["algorithm", "level"]] = (
    mean_energy["project_name"].str.split("-", expand=True)
)

# Level sırası (grafik düzgün çıksın diye)
level_order = ["low", "medium", "high"]

# 5️⃣ HER ALGORİTMA İÇİN TABLO + GRAFİK
for algo in mean_energy["algorithm"].unique():

    algo_data = mean_energy[
        mean_energy["algorithm"] == algo
    ][["level", "energy_consumed"]]

    # Level sırasına göre sırala
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

    # Dosyaya kaydet
    filename = f"{algo.lower()}_energy.png"
    plt.savefig(filename, dpi=300)
    plt.show()
