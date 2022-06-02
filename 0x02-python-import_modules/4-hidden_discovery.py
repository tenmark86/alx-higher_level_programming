#!/usr/bin/python3
import hidden_4


def main():
    for i in dir(hidden_4):
        if i[0] != '_' and i[1] != '_':
            print("{}".format(i))
if __name__ == "__main__":
    main()
