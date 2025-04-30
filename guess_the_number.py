import random

num = random.randint(1,99)
attempt = 1
def fun(attempt) :
    n = int(input("guess the number (1-9)"))
    if num != n:
        if n> num:
            print("too high")
            fun(attempt +1)
        else:
            print("too low")
            fun(attempt +1)
    else :    
        print("you guess the right number in ", attempt , "attempt")
fun(attempt)
