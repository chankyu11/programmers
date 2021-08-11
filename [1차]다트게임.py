# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    n = ''
    res = []
   
    for i in dartResult:
        if i.isdigit():
            n += i
            print(n)
        elif i == 'S':
            n = int(n)**1
            res.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            res.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            res.append(n)
            n = ''
        elif i == '*':
            if len(res) > 1:
                res[-2] = res[-2] * 2
                res[-1] = res[-1] * 2
            else:
                res[-1] = res[-1] * 2
        elif i == '#':
            res[-1] = res[-1] * -1

    return sum(res)