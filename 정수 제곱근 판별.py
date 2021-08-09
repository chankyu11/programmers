# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    answer = 0
    a = n ** 0.5
    if a == int(a):
        answer += (a+1) * (a+1)
    else:
        answer += -1
  
    
    return answer