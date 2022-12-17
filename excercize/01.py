'''
Esercizio 001: Max tra Due Numeri
Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.
'''

def bigger_number(number_one, number_two):
    if number_one == number_two:
        return "pair"
    else if number_one > number_two:
        return number_one
    elif number_one < number_two:
        return number_two        