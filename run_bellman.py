import csv
from bellman_ford import bellman_ford
from data_generator import generate_graph
from energy_measure import measure

sizes = {
    "low": (50, 200),
    "medium": (200, 2000),
    "high": (500, 8000)
}

with open("bellman_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["level", "vertices", "edges", "time_sec", "cpu_time"])

    for level, (v, e) in sizes.items():
        vertices, edges = generate_graph(v, e)

        time_sec, cpu_time, _ = measure(
            bellman_ford,
            vertices,
            edges,
            0
        )

        writer.writerow([level, v, e, time_sec, cpu_time])

        print(f"{level.upper()} saved.")
