from algorithms.floyd_warshall import floyd_warshall
from data_generator import generate_matrix
from energy_measure import measure

sizes = {
    "low": 50,
    "medium": 150,
    "high": 300
}

for level, n in sizes.items():
    graph = generate_matrix(n)

    time_sec, cpu_time, energy_kwh, _ = measure(
        floyd_warshall,
        f"FloydWarshall-{level}",
        graph
    )

    print(
        f"{level.upper()} | N={n} | "
        f"Time={time_sec:.4f}s | "
        f"Energy={energy_kwh:.2e} kWh"
    )
