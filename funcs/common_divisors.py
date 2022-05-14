import numpy as np


def gcd(n1, n2):
    gcd = np.arange(1, np.sort(np.array([n1, n2]) + 1)[0])
    gcd = gcd[(n1 % gcd == 0) & (n2 % gcd == 0)][-1]
    return f"gcd: {gcd}"


def input_():
    while True:
        numbers = input(
            "enter 2 numbers to find the common divisors(ex. 5 10):\n").split(" ")
        try:
            n1 = int(numbers[0])
            n2 = int(numbers[1])
        except ValueError:
            raise Exception("Please enter an integer")
        except IndexError:
            raise Exception("Please enter 2 numbers")
        else:
            print(gcd(n1, n2))
            continue


# input_()
