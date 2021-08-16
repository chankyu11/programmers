# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    
    answer.reverse()
    return answer

# pythonic

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]