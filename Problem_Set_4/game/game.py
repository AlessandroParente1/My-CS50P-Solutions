import random

def get_positive_int(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level
        except ValueError:
            pass  # Se l'input non è un numero, ripeti la richiesta

def main():
    level = get_positive_int("Level: ")  # Richiede il livello
    number = random.randint(1, level)  # Genera un numero casuale tra 1 e level

    while True:
        guess = get_positive_int("Guess: ")  # Richiede il tentativo dell'utente

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:  # Se il tentativo è uguale al numero
            print("Just right!")
            break # Esce dal ciclo quando l'utente indovina il numero

if __name__ == "__main__":
    main()
