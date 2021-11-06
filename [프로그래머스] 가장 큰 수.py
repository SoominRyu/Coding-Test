from itertools import permutations

def solution(numbers):
    num = [0]

    for i in permutations(numbers, len(numbers)):
        num1 = []
        for i in list(str(i)):
            if i.isdigit():
                num1.append(i)
        
        if int(''.join(num1)) > int(num[0]):      
            num[0] = (''.join(num1))


    return num[0]
