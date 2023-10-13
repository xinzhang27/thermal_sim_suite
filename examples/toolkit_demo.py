# This file is an example of how to use the property.py
from src.toolkit.property import Material, Searcher, METAL_PATH

# Get the metal data
metal_data = Searcher(METAL_PATH)

# Search for materials containing 'Aluminum' in their name
aluminum_datas = metal_data.search('Aluminum')
print("Materials containing 'Aluminum' in their name:", aluminum_datas)

# Get properties for a specific material by ID
aluminum_data = metal_data.get_properties(4)
print("Properties for one aluminum alloy:", aluminum_data)

# Create a material object which can be easily to get the properties
aluminum = Material(**aluminum_data)
print("Density of the aluminum alloy:", aluminum.density)
print("Number of the density:", aluminum.density_num)
print("Unit of the density:", aluminum.density_unit)
