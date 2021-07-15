# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3)
        # divmod는 몫과 나머니를 알려줌.
        answer += str(rest)
    answer = int(answer, 3)
    #int는 진법 변환을 지원함

    return answer