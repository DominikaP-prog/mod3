def is_palindrome(word):
    # Usuń spacje i zamień na małe litery dla dokładnego porównania
    word = word.replace(" ", "").lower()
    # Sprawdź, czy wyraz czytany od przodu i od tyłu jest taki sam
    return word == word[::-1]

# Przykładowe użycie funkcji
print(is_palindrome("kajak"))  # True
print(is_palindrome("potop"))  # True
print(is_palindrome("palindrom"))  # False