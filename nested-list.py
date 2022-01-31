#!/usr/bin/python

import math

def second_lowest(records):
    first = second = [math.inf,math.inf]

    for student in  records:

        if student[1] < first[1]:
            second = first
            first = student
        elif student[1] < second[1] and student[1] != first[1]:
            second = student
    
    return second

if __name__ == '__main__':

    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    

    names = []
    names.append(second_lowest(records)[0])
    for i in records:
        if i[1] == second_lowest(records)[1]:
            names.append(i[0])

    names = list(set(names))
    names.sort()
    for name in names:
        print(name)
