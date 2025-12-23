import csv

from bellman_ford import bellman_ford
from floyd_warshall import floyd_warshall
from knapsack import knapsack

from data_generator import (
    generate_graph,
    generate_matrix,
    generate_knapsack_data
)

from energy_measure import measure

with open("all_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["algorithm", "input_level", "n", "time_sec", "cpu_time"])

    # ---------------- Bellman–Ford ----------------
    bf_sizes = {
        "low": (50, 200),
        "medium": (200, 2000),
        "high": (500, 8000)
    }

    for level, (v, e) in bf_sizes.items():
        vertices, edges = generate_graph(v, e)
        time_sec, cpu_time, _ = measure(bellman_ford, vertices, edges, 0)
        writer.writerow(["Bellman-Ford", level, v, time_sec, cpu_time])

    # ---------------- Floyd–Warshall ----------------
    fw_sizes = {
        "low": 50,
        "medium": 150,
        "high": 300
    }

    for level, n in fw_sizes.items():
        matrix = generate_matrix(n)
        time_sec, cpu_time, _ = measure(floyd_warshall, matrix)
        writer.writerow(["Floyd-Warshall", level, n, time_sec, cpu_time])

    # ---------------- Knapsack ----------------
    ks_sizes = {
        "low": (50, 100),
        "medium": (200, 500),
        "high": (500, 1000)
    }

    for level, (n, cap) in ks_sizes.items():
        w, v, c = generate_knapsack_data(n, cap)
        time_sec, cpu_time, _ = measure(knapsack, w, v, c)
        writer.writerow(["Knapsack", level, n, time_sec, cpu_time])

print("All experiments completed.")
