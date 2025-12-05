import pandas as pd

data = {
    "nr_id": [1, 2, 3, 4, 5],
    "imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "wiek": [35, 28, 40, 30, 45],
    "pensja": [8000, 4500, 6000, 5500, 7000]
}

df = pd.DataFrame(data)
print(df)

#a)
pensja_5000_ponad = df[df["pensja"]>5000]
print(f"\nPracownicy z pensją wyższą od 5000: \n{pensja_5000_ponad}")

#b)
df_sort_wiek = df.sort_values(by="wiek")
print(f"\nPracownicy wg wieku: \n{df_sort_wiek}")

#c)
df_group_stanowisko = df.groupby("stanowisko")["pensja"].mean()
print(f"\nŚrednia pensja pracowników wg stanowiska: \n{df_group_stanowisko}")

#d)
awans = {
    "nr_id": [1, 5],
    "nowe_stanowisko": ["Starszy manager", "Dyrektor"],
    "nowa_pensja": [10000, 12000]
}
df_awans = pd.DataFrame(awans)
df_combined = pd.merge(df, df_awans, on = "nr_id", how = "left")
print(f"Dane pracowników po awansie: \n{df_combined}")

#e)
df_combined.to_csv("pracownicy.csv", index = False)
print("Dane zapisane do pliku: 'pracownicy.csv'")

#f)
df_from_csv = pd.read_csv("pracownicy.csv")
print(f"Dane z pliku 'pracownicy.csv': \n{df_from_csv}")