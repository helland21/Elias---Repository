def my_max(lst):
    if len(lst) == 1: #Basis-tilfellet: En liste med en verdi eller et tall, som gjør at verdien er den største 
        return lst[0]
    else:
        #Sammenligner første element med den største verdien i listen
        max_of_rest = my_max(lst[1:])
        if lst[0] > max_of_rest:
            return lst[0]
        else:
            return max_of_rest

print(my_max([1, 2, 3, 4, 5]))
print(my_max([100, 200, 300, 400, 500]))
print(my_max([100/50, 600/50, 700/50, 800/50]))