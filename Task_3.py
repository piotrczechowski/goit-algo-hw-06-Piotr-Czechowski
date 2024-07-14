import networkx as nx
import matplotlib.pyplot as plt
import heapq


G = nx.Graph()


nodes = ["Station A", "Station B", "Station C", "Station D", "Station E"]
edges = [
    ("Station A", "Station B", 10),
    ("Station A", "Station C", 15),
    ("Station B", "Station D", 20),
    ("Station C", "Station D", 25),
    ("Station D", "Station E", 30),
    ("Station E", "Station A", 35)
]


G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Layout for the visualization
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_weight="bold", edge_color="gray")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Transportation Network Graph")
plt.show()

# Implement Dijkstra's algorithm to find shortest paths
def dijkstra(graph, start):
    queue = [(0, start, [])]
    seen = set()
    min_dist = {start: 0}
    paths = {start: []}
    
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in seen:
            continue
        seen.add(node)
        path = path + [node]
        for next_node, distance in graph[node].items():
            if next_node in seen:
                continue
            prev_cost = min_dist.get(next_node, float('inf'))
            new_cost = cost + distance['weight']
            if new_cost < prev_cost:
                min_dist[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node, path))
                paths[next_node] = path

    return min_dist, paths

all_shortest_paths = {}
for node in G.nodes:
    distances, paths = dijkstra(G, node)
    all_shortest_paths[node] = (distances, paths)

# Display the shortest paths and their respective costs
def display_shortest_paths(shortest_paths):
    for start_node, (distances, paths) in shortest_paths.items():
        print(f"Shortest paths from {start_node}:")
        for end_node in G.nodes:
            if start_node != end_node:
                print(f"  To {end_node}: Path: {' -> '.join(paths[end_node] + [end_node])}, Cost: {distances[end_node]}")
        print("\n")

display_shortest_paths(all_shortest_paths)
