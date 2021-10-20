def solution(s):
    answer = ''
    a = len(s)
    if (a%2 == 0):
        answer = s[a//2-1] + s[a//2]
    else:
        answer = s[a//2]
    return answer
