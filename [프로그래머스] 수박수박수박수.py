def solution(n):
    answer = ''
    repeat = n//2
    if n%2 == 1:
        answer = repeat * '수박' + '수'
    else:
        answer = repeat * '수박'
    return answer
