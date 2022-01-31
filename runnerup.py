#!/usr/bin/python

def first_method(score_sheet):
    winner, runner_up = max(score_sheet[0], score_sheet[1]), min(score_sheet[0], score_sheet[1])

    for i in range(2, len(score_sheet)):
        if score_sheet[i] > winner:
            runner_up = winner
            winner = score_sheet[i]
        elif score_sheet[i] > runner_up and score_sheet[i] != winner: #No need the second condition because of set function
            runner_up = score_sheet[i]
    
    return runner_up

def second_method(score_sheet):
    score_sheet.sort()
    return score_sheet[len(score_sheet) -2]

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))

    print(first_method(arr))