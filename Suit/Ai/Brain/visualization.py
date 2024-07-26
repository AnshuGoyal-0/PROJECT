# visualization.py

import networkx as nx
import matplotlib.pyplot as plt

def visualize_mind_map(root):
    G = nx.DiGraph()

    def add_edges(node):
        for child in node.children:
            G.add_edge(node.name, child.name)
            add_edges(child)
    
    add_edges(root)
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=10, font_weight="bold", edge_color="gray")
    plt.title("Mind Map Visualization")
    plt.show()
