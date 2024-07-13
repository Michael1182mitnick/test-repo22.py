# fibonacci series using def function in python

def fibon(number):
    first, second = 0, 1
    if  number == 1:
        print(first)
    if number <= 0:
        print("Please enter a number greater than zero")
    else:
        print("Fibonacci series are")
        print(first, end=" ")
        print(second, end=" ")
        for i in range(2, number):
            next = first + second
            first = second
            second = next 
            print(next, end=" ")  
digit = int(input("Enter any numbers: "))
fibon(digit)   