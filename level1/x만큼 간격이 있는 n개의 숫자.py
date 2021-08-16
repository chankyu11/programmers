# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(i*x+x)
    
    return answer
'''
x = 2
n = 5
i = 0,1,2,3,4
i*x = 0,2,4,6,8
i*x+x = 2,4,6,8,10

x = 4
n = 3
i = 0,1,2
i*x = 0,4,8
i*x+x = 4,8,12

x = -4
n = 2
i = 0,1
i*x = 0,-4,
i*x+x = -4,-8,
'''