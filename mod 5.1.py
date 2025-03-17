pip install faker 

from faker import Faker


# Definiowanie klasy reprezentującej wizytówkę
class BusinessCard:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

# Funkcja tworząca instancje klasy BusinessCard z losowymi danymi
def create_random_business_card():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    return BusinessCard(first_name, last_name, email)

# Tworzenie listy 5 wizytówek z losowymi danymi
business_cards = [create_random_business_card() for _ in range(5)]

# Wyświetlanie zawartości listy wizytówek
for card in business_cards:
    print(card)