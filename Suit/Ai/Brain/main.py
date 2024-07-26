# main.py

from mind_map import MindMap
from data_categorization import categorize_data
from mind_map_linking import link_mind_maps
from visualization import visualize_mind_map
from category_map import create_category_map

# Initialize mind maps
user_info_map = MindMap("User Information", "Stores user profile data")
family_info_map = MindMap("Family Information", "Stores family-related data")

# Example data
user_data = {'type': 'User Information', 'id': 'user1', 'name': 'John Doe', 'age': 30}
family_data = {'type': 'Family Information', 'id': 'family1', 'members': ['John Doe', 'Jane Doe']}

# Add your name data
personal_info = {'type': 'User Information', 'id': 'anshu', 'name': 'Anshu Goyal'}

# Categorize and store data
mind_maps = {'User Information': user_info_map, 'Family Information': family_info_map}
categorize_data(user_data, mind_maps)
categorize_data(family_data, mind_maps)
categorize_data(personal_info, mind_maps)

# Link mind maps (optional)
link_mind_maps(user_info_map, family_info_map, 'user1', 'family1')

# Create and visualize category map
category_map = create_category_map(mind_maps)
visualize_mind_map(category_map)

# Visualize individual mind maps
visualize_mind_map(user_info_map)
visualize_mind_map(family_info_map)
