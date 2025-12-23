from floyd_warshall import floyd_warshall
from data_generator import generate_matrix
from energy_measure import measure

sizes = {
    "low": 50,
    "medium": 150,
    "high": 300
}

for level, n in sizes.items():
    graph = generate_matrix(n)

    time_sec, cpu_time, _ = measure(
        floyd_warshall,
        graph
    )

    print(f"{level.upper()} | N={n} | Time={time_sec:.4f}s | CPU={cpu_time:.4f}s")
