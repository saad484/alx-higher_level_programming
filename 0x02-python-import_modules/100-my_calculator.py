#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == "+":
        res = a + b
        print("{} {} {} = {}".format(a, operator, b, res))
    elif operator == "-":
        res = a - b
        print("{} {} {} = {}".format(a, operator, b, res))
    elif operator == "*":
        res = a * b
        print("{} {} {} = {}".format(a, operator, b, res))
    elif operator == "/":
        res = a / b
        print("{} {} {} = {}".format(a, operator, b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
