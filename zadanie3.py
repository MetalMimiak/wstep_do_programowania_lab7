import pandas as pd

df = pd.read_csv('demografia.csv')
print(df)

df = pd.read_csv('demografia.csv', decimal = ',', na_values = ['NA', 'n/a', 'NaN'])

df_bez_kraju = df.drop(columns = ['KRAJE'])
max_przyrost = df_bez_kraju.max().max()
print(max_przyrost)

max_przyrost_rok = df_bez_kraju.max().idxmax()
max_przyrost_index = df_bez_kraju[max_przyrost_rok].idxmax()
max_przyrost_kraj = df.loc[max_przyrost_index, 'KRAJE']

print(f"Największy przyrost ludności wyniósł {max_przyrost} i miał miejsce w {max_przyrost_rok} w {max_przyrost_kraj}")