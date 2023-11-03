#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == "+":
        res = add(a, b)
        print("{} {} {} = {}".format(a, op, b, res))
    elif op == "-":
        res = sub(a, b)
        print("{} {} {} = {}".format(a, op, b, res))
    elif op == "*":
        res = mul(a, b)
        print("{} {} {} = {}".format(a, op, b, res))
    elif op == "/":
        res = div(a, b)
        print("{} {} {} = {}".format(a, op, b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
