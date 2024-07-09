#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for number in num_list:
        if (number % 2 == 0):
            evens.append(number)
    
    print(evens)

return_evens([0, 1, 3, 5, 7, 8, 9])      

def make_exclamation(sentence_list):
    pass