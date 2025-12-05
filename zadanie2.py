import pandas as pd

df = pd.read_csv('demografia.csv')

max_przyrost_index = df['2022'].idxmax(skipna = True)
max_przyrost_kraj = df.loc[max_przyrost_index, 'KRAJE']

print(f"Kraj z największym przyrostem ludzi w 2022 roku: {max_przyrost_kraj}")