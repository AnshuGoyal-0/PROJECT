# data_categorization.py

def categorize_data(data, mind_maps):
    category = data.get('type')
    if category in mind_maps:
        mind_map = mind_maps[category]
    else:
        # Create new category if it doesn't exist
        new_category_name = category
        mind_map = MindMap(new_category_name, f"Category for {category} data")
        mind_maps[new_category_name] = mind_map
    
    mind_map.add_node(data['id'], data)
    return mind_map
