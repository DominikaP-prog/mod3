import logging

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(message)s')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def main():
    # Pobierz typ operacji od użytkownika
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

    # Pobierz dwie liczby od użytkownika
    num1 = float(input("Podaj składnik 1: "))
    num2 = float(input("Podaj składnik 2: "))

    # Wykonaj operację i zaloguj szczegóły
    if operation == '1':
        logging.info(f"Dodaję {num1:.2f} i {num2:.2f}")
        result = add(num1, num2)
    elif operation == '2':
        logging.info(f"Odejmuję {num1:.2f} i {num2:.2f}")
        result = subtract(num1, num2)
    elif operation == '3':
        logging.info(f"Mnożę {num1:.2f} i {num2:.2f}")
        result = multiply(num1, num2)
    elif operation == '4':
        logging.info(f"Dzielę {num1:.2f} i {num2:.2f}")
        result = divide(num1, num2)
    else:
        result = "Error: Invalid operation"

    # Drukuj wynik
    print(f"Wynik to {result}")

if __name__ == "__main__":
    main()

    