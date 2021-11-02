def solution(s):
    s1 = list(s)
    if s1[0].isdigit() == True or s1[0] == '+':
        answer = int(s)
    else:
        answer = -1 * int("".join(s1[1:]))
    return answer
