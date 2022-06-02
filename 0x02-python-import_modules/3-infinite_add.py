#!/usr/bin/python3
import sys


def main():
    sumita = 0
    for i in range(1, len(sys.argv)):
        sumita += int(sys.argv[i])
    print("{:d}".format(sumita))
if __name__ == "__main__":
    main()
