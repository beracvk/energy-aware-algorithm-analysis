import random

def generate_graph(vertices, edges):
    edge_list = []

    for _ in range(edges):
        u = random.randint(0, vertices - 1)
        v = random.randint(0, vertices - 1)
        weight = random.randint(-10, 20)
        edge_list.append((u, v, weight))

    return vertices, edge_list

def generate_matrix(n):
    INF = 10**9
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            else:
                # %70 ihtimalle kenar var
                if random.random() < 0.7:
                    row.append(random.randint(1, 10))
                else:
                    row.append(INF)
        matrix.append(row)

    return matrix

def generate_knapsack_data(n, capacity):
    import random

    weights = [random.randint(1, 20) for _ in range(n)]
    values = [random.randint(10, 100) for _ in range(n)]

    return weights, values, capacity


