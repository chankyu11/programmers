# https://programmers.co.kr/learn/courses/30/lessons/12919


def solution(seoul):
    answer = ''
    for i,s in enumerate(seoul):
        if s == 'Kim':
            answer += str(i)
    
    res = f'김서방은 {answer}에 있다'
    return res



# pythonic
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
    