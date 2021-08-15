# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = 1
    res = []
    
    for i in s:
        if i not in res:
            res.append(i)
        elif i == res[-1]:
            res.pop()
    if len(res) > 0:
        answer -= 1

    return answer