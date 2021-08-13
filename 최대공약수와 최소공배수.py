# https://programmers.co.kr/learn/courses/30/lessons/12940

def gcd(x, y):
    while y:
        x,y = y,x%y
    return x

def solution(x, y):
    
    return [gcd(x, y),x * y // gcd(x, y)]