# https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3

def solution(nums):
    unique_types = len(set(nums))

    if len(nums) / 2 > unique_types:
        return unique_types
    else:
        return len(nums) / 2




# pythonic
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
