# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    
    s = str(n)
    s = ''.join(sorted(s, reverse = True))
    return int(s)