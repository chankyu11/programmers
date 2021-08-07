# https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1,arr2):
        tmp = []
        for m in range(len(i)):
            tmp.append(i[m]+j[m])
        answer.append(tmp)

    return answer


def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
    return answer