# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = False
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True
        
    return answer

#pythonic

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)