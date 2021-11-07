def solution(s):
    # answer = ''
    emp = []
    hap = []
    for i in range(len(s)):
        if s[i] == " ":
            emp.append(i)
    
    s1 = s.split()
    for j in s1:
        j1 = list(j)
        for k in range(len(j1)):
            if k % 2 == 0:
                hap.append(j1[k].upper())
            else:
                hap.append(j1[k].lower())
    for e in emp:
        hap.insert(e, ' ')

    return ''.join(hap)
