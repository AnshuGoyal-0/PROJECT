# category_map.py

from mind_map import MindMap

def create_category_map(mind_maps):
    category_map = MindMap("Category Map", "Overview of all categories and their descriptions")
    for category, mind_map in mind_maps.items():
        category_map.add_node(category, {'description': mind_map.description})
    return category_map
