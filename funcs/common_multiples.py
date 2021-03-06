import numpy as np


def lcm(n1, n2):
    cm = []
    bignum = np.sort(np.array([n1, n2]))[-1]
    smallnum = np.sort(np.array([n1, n2]))[0]
    numbers = np.arange(1, bignum + 1)
    gcd = np.arange(1, smallnum + 1)
    gcd = gcd[(n1 % gcd == 0) & (n2 % gcd == 0)][-1]
    for i in numbers:
        if smallnum * i == bignum:
            cm.append(smallnum * i)
        elif smallnum == bignum:
            cm.append(smallnum)
            break
        else:
            cm.append(int(round((smallnum * bignum)/gcd)))
    cm = np.sort(np.unique(cm))
    return f"lcm: {cm[0]}"


def input_():
    while True:
        numbers = input(
            "enter 2 numbers to find the common multiples(ex. 5 10):\n").split(" ")
        try:
            n1 = int(numbers[0])
            n2 = int(numbers[1])
        except ValueError:
            raise Exception("Please enter an integer")
        except IndexError:
            raise Exception("Please enter 2 numbers")
        else:
            print(lcm(n1, n2))  # 0.0020492076873779297
            continue
