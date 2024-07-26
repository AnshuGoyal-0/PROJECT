# visualization.py

import networkx as nx
import matplotlib.pyplot as plt

def add_edges(node, G):
    for child in node.children:
        G.add_edge(node.name, child.name)
        add_edges(child, G)

def visualize_mind_map(mind_map):
    G = nx.DiGraph()
    
    # Assume root nodes are directly added to the graph
    for node_name, node in mind_map.nodes.items():
        G.add_node(node_name)
        add_edges(node, G)
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=10, font_weight="bold", edge_color="gray")
    plt.title(f"Mind Map Visualization: {mind_map.name}")
    plt.show()
