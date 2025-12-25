import pandas as pd 

df = pd.read_csv("emissions.csv")
print(df.head())

energy_df = df[[
    "project_name", "duration", "energy_consumed"
]]

mean_energy = (
    energy_df
    .groupby("project_name")
    .mean()
    .reset_index()
)

print(mean_energy)