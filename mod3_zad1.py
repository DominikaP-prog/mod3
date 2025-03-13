#Zadanie 1
zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for sklep, rzeczy in zakupy.items():
    rzeczy_wielka_litera = [rzecz.capitalize() for rzecz in rzeczy]
    print(f"Idę do {sklep.capitalize()} i kupuję tam {', '.join(rzeczy_wielka_litera)}.")

suma_produktow = sum(len(rzeczy) for rzeczy in zakupy.values())
print(f"W sumie kupuję {suma_produktow} produktów.")


#Zadanie 2

liczby_podzielne_przez_5 = [liczba for liczba in range(101) if liczba % 5 == 0]
print("Liczby podzielne przez 5:", liczby_podzielne_przez_5)


liczby_podniesione_do_3 = [liczba ** 3 for liczba in liczby_podzielne_przez_5]
print("Liczby podzielne przez 5 podniesione do potęgi 3:", liczby_podniesione_do_3)