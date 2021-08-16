# https://programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    wi = w
    he = h
    
    while (wi != he):
        if wi > he:
            wi -= he
        else: 
            he -= wi
    return w*h - (w+h - he)