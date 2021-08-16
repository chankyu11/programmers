# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        dot = a[i] * b[i]
        answer += dot
    return answer