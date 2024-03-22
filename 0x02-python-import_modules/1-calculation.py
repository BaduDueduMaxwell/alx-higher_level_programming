#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    add_num = add(a, b)
    sub_num = sub(a, b)
    mul_num = mul(a, b)
    div_num = div(a, b)

    print("{} + {} = {}".format(a, b, add_num))
    print("{} - {} = {}".format(a, b, sub_num))
    print("{} * {} = {}".format(a, b, mul_num))
    print("{} / {} = {}".format(a, b, div_num))
