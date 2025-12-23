from knapsack import knapsack
from data_generator import generate_knapsack_data
from energy_measure import measure

sizes = {
    "low": (50, 100),
    "medium": (200, 500),
    "high": (500, 1000)
}

for level, (n, cap) in sizes.items():
    weights, values, capacity = generate_knapsack_data(n, cap)

    time_sec, cpu_time, _ = measure(
        knapsack,
        weights,
        values,
        capacity
    )

    print(f"{level.upper()} | N={n} | Time={time_sec:.4f}s | CPU={cpu_time:.4f}s")
