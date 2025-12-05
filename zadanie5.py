import pandas as pd

dane_studentow = {
    "nr_albumu": [1, 2, 3, 4, 5],
    "imię": ["Anna", "Jan", "Katarzyna", "Tpmasz", "Michał"],
    "nazwisko": ['Kowalska', "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "ocena": [4.5, 3.0, 5.0, 4.0, 2.5],
    "wiek": [22, 21, 24, 23, 25]
}

df_dane_studentow = pd.DataFrame(dane_studentow)
print(df_dane_studentow)

#a)
studenci_4_powyzej = df_dane_studentow[df_dane_studentow["ocena"] > 4]
print(f"\nStudenci z wyższą oceną niż 4: \n{studenci_4_powyzej}")

#b)
studenci_sort_wiek = df_dane_studentow.sort_values(by = "wiek")
print(f"\nStudenci wg wieku: \n{studenci_sort_wiek}")

#c)
srednia_wieku_wg_ocen = df_dane_studentow.groupby("ocena")["wiek"].mean().reset_index()
print(f"\nŚrednia wieku studenów wg ocen: \n{srednia_wieku_wg_ocen}")

#d)
dane_z_poprawy = {
    "nr_albumu": [1, 2, 5],
    "ocena_z_poprawy": [5.0, 4.0, 3.5]
}
df_poprawa = pd.DataFrame(dane_z_poprawy)
df_combined = pd.merge(
    df_dane_studentow,
    df_poprawa,
    on = "nr_albumu",
    how = "left"
)
print(f"\nDane z danymi z poprawy: \n{df_combined}")

#e)
nazwa_pliku = "dane_studentow_poprawa.csv"
df_combined.to_csv(nazwa_pliku, index = False)
print(f"Zapisano dane do pliku: '{nazwa_pliku}'")

#f)
df_wczytany_plik = pd.read_csv(nazwa_pliku)
print(f"Wczytano dane z pliku: '{nazwa_pliku}'")
print(df_wczytany_plik.head())

#g)
nowy_student = {
    "nr_albumu": 6,
    "imię": "Agnieszka",
    "nazwisko": "Lew",
    "ocena": 4.5,
    "wiek": 20
}
df_nowy_student = pd.DataFrame([nowy_student])
df_dane_studentow_nowe = pd.concat([df_dane_studentow, df_nowy_student], ignore_index = True)
print(f"\nNowe dane studenów z uwzględnieniem nowego studenta: \n{df_dane_studentow_nowe}")

#h)
unikalne_wartosci_ocen = df_dane_studentow_nowe["ocena"].unique()
print(f"\nUnikalne wartości ocen: \n{unikalne_wartosci_ocen}")

#i)
liczba_studentow_ma_5 = (df_dane_studentow_nowe["ocena"] == 5.0).sum()
print(f"\nLiczba studentów z oceną równą 5: \n{liczba_studentow_ma_5}")