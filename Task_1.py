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
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_weight="bold", edge_color="gray")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Transportation Network Graph")
plt.show()


num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_vertices = dict(G.degree())

print(f"Number of vertices: {num_vertices}")
print(f"Number of edges: {num_edges}")
print("Degree of each vertex:")
for node, degree in degree_of_vertices.items():
    print(f"{node}: {degree}")
