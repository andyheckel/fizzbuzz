#!/usr/bin/python3

def fiz_div(number):
    return (number % 3 == 0, number % 5 == 0)

for i in range(1,101):
   # print(fiz_div(i))
    if (fiz_div(i) == (True, True)):
        print("FizzBuzz")
    elif (fiz_div(i) == (True, False)):
        print("Fizz")
    elif (fiz_div(i) == (False, True)):
        print("Buzz")
    else:
        print(str(i))

