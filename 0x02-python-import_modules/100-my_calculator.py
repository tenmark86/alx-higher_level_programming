#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        sign = ['+', '-', '*', '/']
        signok = 0
        for i in sign:
            if sys.argv[2] == i:
                signok = 1
                break
        if signok == 0:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = sys.argv[1]
            b = sys.argv[3]
            if sys.argv[2] == sign[0]:
                print("{:s} + {:s} = {:d}".format(a, b, add(int(a), int(b))))
            elif sys.argv[2] == sign[1]:
                print("{:s} - {:s} = {:d}".format(a, b, sub(int(a), int(b))))
            elif sys.argv[2] == sign[2]:
                print("{:s} * {:s} = {:d}".format(a, b, mul(int(a), int(b))))
            elif sys.argv[2] == sign[3]:
                print("{:s} / {:s} = {:d}".format(a, b, div(int(a), int(b))))
if __name__ == "__main__":
    main()
