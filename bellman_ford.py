def bellman_ford(vertices, edges, source):
    """
    vertices: grafın kaç düğümü olduğu (int)
    edges: [(u, v, weight), ...] kenar listesi
    source: başlangıç düğümü
    """

    # 1️⃣ Her düğüme olan mesafeyi sonsuz yap
    distance = [float('inf')] * vertices

    # 2️⃣ Kaynağın mesafesi 0
    distance[source] = 0

    # 3️⃣ V-1 kere tüm kenarları kontrol et
    for i in range(vertices - 1):
        for u, v, weight in edges:
            # Eğer u'ya ulaşabiliyorsam ve
            # u üzerinden v daha kısa oluyorsa → güncelle
            if distance[u] != float('inf'):
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    return distance
