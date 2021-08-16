# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    i = 0
    
    while True:
        if num == 1:
            break
        if i == 500:
            break
        if num % 2 == 0:
            num = num / 2
            i += 1
        else:
            num = num * 3 +1
            i += 1
        
    if i != 500:
        i = i
    else:
        i = -1
    return i