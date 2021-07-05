# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations


def solution(nums):
    answer = 0
    cb = list(combinations(nums, 3))
    for i in cb:
        cb_sum = sum(i)
        prime = True
        for j in range(2, int(cb_sum ** 0.5)+1):
            if cb_sum % j == 0:
                prime = False
                
        if prime:
            answer += 1
    
    return answer