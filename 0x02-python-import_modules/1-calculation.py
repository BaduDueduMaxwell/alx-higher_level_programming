#!/usr/bin/python3
<<<<<<< HEAD
if __name__ = "__main__":
    import calculator_1 as add, sub, mul, div
=======
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
>>>>>>> 76684a2bea48083fd232b4a1c303caa9bc5452ab
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
