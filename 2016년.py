# https://programmers.co.kr/learn/courses/30/lessons/12901

import datetime

def solution(a, b):

    date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = date[datetime.datetime(2016, a, b).weekday()]
    return answer