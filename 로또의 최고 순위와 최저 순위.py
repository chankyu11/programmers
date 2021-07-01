# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    
    rank, c_z = 7, 0

    for num in lottos:
        if num in win_nums:
            rank -= 1
        elif num == 0:
            c_z += 1
    
    return [min(rank - c_z,6), min(rank, 6)]