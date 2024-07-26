# mind_map_linking.py

def link_mind_maps(mind_map1, mind_map2, node_name1, node_name2):
    mind_map1.add_link(node_name1, mind_map2.name, node_name2)
    mind_map2.add_link(node_name2, mind_map1.name, node_name1)
