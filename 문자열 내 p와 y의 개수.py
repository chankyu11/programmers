# https://programmers.co.kr/learn/challenges

def solution(s):
    answer = True
    c_p = 0
    c_y = 0
    for i in s.lower():
        if i == 'p':
            c_p += 1
        elif i == 'y':
            c_y += 1
    if c_p != c_y:
        answer = False
    
    
    return answer

# pythonic

def solution(s):
    return s.lower().count('p') == s.lower().count('y')