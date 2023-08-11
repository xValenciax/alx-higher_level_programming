#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    len = len(sys.argv) - 1

    if len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, op, b = sys.argv[1:]
    a = int(a)
    b = int(b)

    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if op == '+':
        print("{} {} {} = {}".format(a, op, b, calc.add(a, b)))
    if op == '-':
        print("{} {} {} = {}".format(a, op, b, calc.sub(a, b)))
    if op == '*':
        print("{} {} {} = {}".format(a, op, b, calc.mul(a, b)))
    if op == '/':
        print("{} {} {} = {}".format(a, op, b, calc.div(a, b)))
