# %%
import pandas as pd

METAL_PATH = '../static/metal_datas.csv'
CERAMIC_PATH = '../static/ceramic_datas.csv'
POLYMER_PATH = '../static/polymer_datas.csv'


# %%
class Material:
    def __init__(self, name, density, elastic_modulus, poisson_ratio, thermal_expansion, thermal_conductivity):
        """
        Initialize the material with its properties
        :type name: str
        :param name: the name of the material
        :type density: str
        :param density: the density of the material
        :type elastic_modulus: str
        :param elastic_modulus: the elastic modulus of the material
        :type poisson_ratio: str
        :param poisson_ratio: the poisson ratio of the material
        :type thermal_expansion: str
        :param thermal_expansion: the thermal expansion coefficient of the material
        :type thermal_conductivity: str
        :param thermal_conductivity: the thermal conductivity coefficient of the material
        """
        self.name = name
        if not pd.isna(density):
            self.density = density
            self.density_num = float(density.split()[0])
            self.density_unit = density.split()[1]
        if not pd.isna(elastic_modulus):
            self.elastic_modulus = elastic_modulus
            self.elastic_modulus_num = float(elastic_modulus.split()[0])
            self.elastic_modulus_unit = elastic_modulus.split()[1]
        if not pd.isna(poisson_ratio):
            self.poisson_ratio = poisson_ratio
            self.poisson_ratio_num = float(poisson_ratio)
            self.thermal_expansion = thermal_expansion
        if not pd.isna(thermal_expansion):
            self.thermal_expansion = thermal_expansion
            self.thermal_expansion_num = float(thermal_expansion.split()[0])
            self.thermal_expansion_unit = thermal_expansion.split()[1]
        if not pd.isna(thermal_conductivity):
            self.thermal_conductivity = thermal_conductivity
            self.thermal_conductivity_num = float(thermal_conductivity.split()[0])
            self.thermal_conductivity_unit = thermal_conductivity.split()[1]

    def __str__(self):
        return self.name


# %%
class Searcher:
    def __init__(self, csv_file):
        """
        Initialize the searcher with the csv file, the file path can be determined by the user
        and the default paths are METAL_PATH, CERAMIC_PATH, POLYMER_PATH
        :type csv_file: str
        :param csv_file: the path to the csv file
        """
        self.data = pd.read_csv(csv_file)
        self.data.set_index('id', inplace=True)

    def search(self, query):
        """
        Fuzzy search for materials containing the query in their name
        :type query: str
        :param query:
        :return: a dataframe containing the name of the materials
        """
        matches = self.data[self.data['name'].str.contains(query, case=False)]
        return matches[['name']]

    def get_properties(self, material_id):
        """
        Get the properties of a material by its ID
        :type material_id: int
        :param material_id:
        :return: a dictionary containing the properties of the material
        """
        if material_id in self.data.index:
            material = self.data.loc[material_id]
            return {
                'name': material['name'],
                'density': material['Density'],
                'elastic_modulus': material['Elastic (Young\'s, Tensile) Modulus'],
                'poisson_ratio': material['Poisson\'s Ratio'],
                'thermal_expansion': material['Thermal Expansion'],
                'thermal_conductivity': material['Thermal Conductivity']
            }
        else:
            return None



