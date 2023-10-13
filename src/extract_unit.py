import pandas as pd

metal = pd.read_csv("../static/metal_datas.csv")
ceramic = pd.read_csv("../static/ceramic_datas.csv")
polymer = pd.read_csv("../static/polymer_datas.csv")
# connect the dataframes to get the full unit
df = pd.concat([metal, ceramic, polymer], ignore_index=True)
print(df.columns)
# find one value for each column which is not NaN
# if there is no such value, the column is marked as "empty"
value_unit_dict = {}
for col in df.columns:
    value_unit_dict[col] = df[col].dropna().iloc[0]

# %%
new_value_unit_dict = {}
for index, value in value_unit_dict.items():
    if index == "id" or index == "name" or index == "genres":
        continue
    if index == "Base Metal Price":
        value = value.replace("relative", "").strip()
    if index == "Embodied Carbon":
        new_value_unit_dict[index] = value
        continue
    if type(value) != str:
        unit = None
    else:
        unit = value.split(" ")[-1]
        try:
            float(unit)
            unit = None
        except ValueError:
            pass

    new_index = f"{index} | {unit}" if unit else index
    # remove unit in value
    new_value = value.replace(unit, "").strip() if unit else value
    new_value_unit_dict[new_index] = new_value

# %%
column_dict = {}
for index, value in value_unit_dict.items():
    if index == "id" or index == "name" or index == "genres":
        column_dict[index] = index
        continue
    if index == "Embodied Carbon":
        column_dict[index] = index
        continue
    if index == "Base Metal Price":
        value = value.replace("relative", "").strip()
    if type(value) != str:
        unit = None
    else:
        unit = value.split(" ")[-1]
        try:
            float(unit)
            unit = None
        except ValueError:
            pass

    new_index = f"{index} | {unit}" if unit else index
    column_dict[index] = new_index

# %%
for index, value in new_value_unit_dict.items():
    lst = index.split(" | ")
    if len(lst) == 1:
        continue
    u = lst[-1].strip()
    print(f"{index} | {u}")


# %%
def get_unit(s: str):
    # if | in s, return the unit
    # else return None
    s_l = s.split(" | ")
    if len(s_l) == 1:
        return None
    return s_l[-1].strip()


# %%
# change the column name to new_value_unit_dict key
df = df.rename(columns=column_dict)
metal = metal.rename(columns=column_dict)
ceramic = ceramic.rename(columns=column_dict)
polymer = polymer.rename(columns=column_dict)

# %%
# remove the unit in the value of df
for df in [metal, ceramic, polymer]:
    for column in df.columns:
        unit = get_unit(column)
        if unit:
            print(f"column: {column}, unit: {unit}")
            df[column] = df[column].apply(lambda x: str(x).replace(unit, "").strip())

# %%
# save the new csv
metal.to_csv("static/metal_datas_with_unit.csv", index=False)
ceramic.to_csv("static/ceramic_datas_with_unit.csv", index=False)
polymer.to_csv("static/polymer_datas_with_unit.csv", index=False)
