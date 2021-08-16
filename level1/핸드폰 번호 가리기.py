# https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3

def solution(phone_number):
    
    l = len(phone_number) - 4
    answer = l*'*' + phone_number[-4:]
  
    return answer



def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]