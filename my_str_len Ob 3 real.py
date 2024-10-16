def my_str_len(s):
    """Beregner lengden av en streng."""
    if s == "":  # Basis-tilfellet: Tom streng
        return 0
    else:
        return 1 + my_str_len(s[1:])  # Legg til 1 og kall rekursivt med resten av strengen

# Teste funksjonen
print(my_str_len("elias"))  # Forventet output: 5
print(my_str_len(""))       # Forventet output: 0
print(my_str_len("abc"))    # Forventet output: 3
print(my_str_len("nicolai")) #Forventet output: 7 
