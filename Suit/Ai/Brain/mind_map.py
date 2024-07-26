# mind_map.py

class Node:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class MindMap:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.nodes = {}

    def add_node(self, node_name, data=None):
        self.nodes[node_name] = Node(node_name, data)

    def add_link(self, node_name, linked_mindmap, linked_node_name):
        if node_name in self.nodes:
            self.nodes[node_name].data = self.nodes[node_name].data or {}
            self.nodes[node_name].data['links'] = self.nodes[node_name].data.get('links', [])
            self.nodes[node_name].data['links'].append((linked_mindmap, linked_node_name))

    def create_category_map(self):
        category_map = MindMap("Category Map", "Overview of all categories and their descriptions")
        return category_map
