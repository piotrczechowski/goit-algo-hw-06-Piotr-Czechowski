import networkx as nx
import matplotlib.pyplot as plt


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



# DFS implementation
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))

# BFS implementation
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))

start_node = "Station A"
goal_node = "Station E"

dfs_result = dfs_path(G, start_node, goal_node)
bfs_result = bfs_path(G, start_node, goal_node)

print(f"DFS path from {start_node} to {goal_node}: {dfs_result}")
print(f"BFS path from {start_node} to {goal_node}: {bfs_result}")

def analyze_paths(dfs_result, bfs_result):
    print("\nAnalysis of paths found:")
    print(f"DFS path length: {len(dfs_result)}")
    print(f"BFS path length: {len(bfs_result)}")
    print("\nExplanation:")
    print("DFS (Depth-First Search) explores as far down one branch before backtracking. It might not find the shortest path.")
    print("BFS (Breadth-First Search) explores all neighbors level by level, ensuring the shortest path in an unweighted graph.")

analyze_paths(dfs_result, bfs_result)
