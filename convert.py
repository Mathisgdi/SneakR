import pandas as pd
import json

# Charger le fichier JSON
with open('data.json') as json_file:
    data = json.load(json_file)

# Convertir le JSON en DataFrame
df = pd.json_normalize(data)

# Exporter le DataFrame en TSV
df.to_csv('data_api.tsv', sep='\t', index=False)
