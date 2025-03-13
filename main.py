#aktualizacja
zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for sklep, rzeczy in zakupy.items():
    rzeczy_wielka_litera = [rzecz.capitalize() for rzecz in rzeczy]
    print(f"Idę do {sklep.capitalize()} i kupuję tam {', '.join(rzeczy_wielka_litera)}.")

suma_produktow = sum(len(rzeczy) for rzeczy in zakupy.values())
print(f"W sumie kupuję {suma_produktow} produktów.")
