import random

def tahiti(x):
    if x != "Dutch":
        return "IT'S john marston micah"
    else:
        return "the iguianas"


def adiviname(x):
    val = [1,2,3,45,2,23432,4,324,234,324,3234,4,34,323,42,432,423,4324,32,432,432,44,32,42]
    guess = random.choice(val)
    print(guess)
    if x == guess:
        return True
    


def run():
    while True:
        x = input("Ingresa tu adivinanza: ")
        if adiviname(x):
            break

        

print(tahiti("Dutch"))

run()