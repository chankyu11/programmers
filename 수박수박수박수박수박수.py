# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    for i in range(n):
        if i % 2==1:
            answer += '박'
        else:
            answer += '수'
        
        
    return answer