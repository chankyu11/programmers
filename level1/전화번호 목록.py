# https://programmers.co.kr/learn/courses/30/lessons/42577


# 효율성에서 실격

def solution(phone_book):
    phone_book.sort()
    
    for p in range(len(phone_book)-1):
        if phone_book[p] in phone_book[p+1]:
            return False
    return True


# startswith이라는 함수는 처음봄.
# 해답.
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

