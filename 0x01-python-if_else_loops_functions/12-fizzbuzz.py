#!/usr/bin/python3
def fizzbuzz():
    s = ''
    for n in range(1,101):
        if n % 3 == 0 and n % 5 == 0:
            s = "FizzBuzz"
        elif n % 3 == 0:
            s = "Fizz"
        elif n % 5 == 0:
            s = "Buzz"
        else:
            s = n
        print(s, end=' ')
