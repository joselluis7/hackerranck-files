#!/usr/bin/python

if __name__ == '__main__':
    n = int(input().strip())

    if n%2 != 0 : print("Weird")
    elif n in range(2,5,2): print("Not Weird")
    elif n in range(6,21,2): print("Weird")
    else: print("Not Weird")