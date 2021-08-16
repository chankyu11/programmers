# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    
    s = str(x)
    tmp = 0
    for i in s:
        tmp+= int(i)
        
          
    return x % tmp ==0