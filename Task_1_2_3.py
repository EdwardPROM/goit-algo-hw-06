import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    graph = nx.Graph()

    american_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
                       "San Diego", "Dallas", "San Jose"]

    graph.add_nodes_from(american_cities)

    edges_with_distances = [
        ("New York", "Los Angeles", 2799),
        ("New York", "Chicago", 791),
        ("Los Angeles", "Chicago", 1744),
        ("Los Angeles", "Houston", 1374),
        ("Los Angeles", "Phoenix", 371),
        ("Chicago", "Houston", 1085),
        ("Chicago", "Phoenix", 1444),
        ("Houston", "Phoenix", 1175),
        ("Houston", "Philadelphia", 1521),
        ("Phoenix", "San Antonio", 1031),
        ("Phoenix", "San Diego", 299),
        ("Philadelphia", "San Antonio", 1560),
        ("San Antonio", "San Diego", 1303),
        ("San Antonio", "Dallas", 274),
        ("San Diego", "Dallas", 1466),
        ("San Diego", "San Jose", 417),
        ("Dallas", "San Jose", 1849)
    ]

    graph.add_weighted_edges_from(edges_with_distances)

    return graph


def describe_graph(graph):
    print(f"Кількість вершин графа: {len(graph.nodes())}")
    print(f"Кількість ребер графа: {graph.number_of_edges()}")
    print(f"Ваги ребер графа: {nx.get_edge_attributes(graph, 'weight')}")

    degree_sequence = dict(graph.degree())
    print(f"Ступені вершин графа:")
    for node, degree in degree_sequence.items():
        print(f"{node}: {degree}")


def visualize_graph(graph):
    weights = nx.get_edge_attributes(graph, "weight")
    max_weight = max(weights.values())
    widths = [w/max_weight * 10 for w in weights.values()]

    pos = nx.spring_layout(graph)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=700,
        node_color="skyblue",
        font_color="black",
        font_size=8,
        edge_color="gray",
        width=widths,
    )
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.show()


def bfs_recursive(graph, start, visited=None, queue=None):
    if visited is None:
        visited = []
    if queue is None:
        queue = [start]

    if not queue:
        return visited

    current_node = queue.pop(0)
    if current_node not in visited:
        visited.append(current_node)
        queue.extend(
            neighbor
            for neighbor in graph.neighbors(current_node)
            if neighbor not in visited
        )

    return bfs_recursive(graph, start, visited, queue)


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = []
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes()}
    distances[start] = 0

    visited = {node: False for node in graph.nodes()}

    while False in visited.values():
        current_node = min(
            [node for node in graph.nodes() if visited[node] is False],
            key=lambda node: distances[node],
        )
        visited[current_node] = True

        for neighbour, weight in graph[current_node].items():
            if distances[current_node] + weight["weight"] < distances[neighbour]:
                distances[neighbour] = distances[current_node] + weight["weight"]

    return distances


if __name__ == "__main__":
    print("")
    print("Завдання 1")
    G = create_graph()
    describe_graph(G)
    print("")
    print("Завдання 2")
    print("DFS-обхід:")
    print(" ".join(dfs_recursive(G, "New York")))

    print("BFS-обхід:")
    print(" ".join(bfs_recursive(G, "New York")))
    print("")
    print("Завдання 3")
    print("Найкоротші відстані від вершини New York:")
    print(dijkstra(G, "New York"))

    visualize_graph(G)
