def solution(s):
    dic = {'zero':'0', 'one':'1', 'two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    key_list = list(dic.keys())
    # print(s.find(key_list[1]))
    an = list(s)
    
    for i in range(len(key_list)):
        #동일 숫자 있는 횟수만큼 반복
        for c in range (s.count(key_list[i])):
            #찾으려는 영단어 시작 인덱스
            sk = s.find(key_list[i])
            #찾은 후 해당 영단어 *로 바꿔주기
            s = s.replace(key_list[i], '*'*len(key_list[i]),1)
            # print(s)
            #찾으려는 영단어가 있는 경우
            if sk != -1:
                an[sk] = dic.get(key_list[i]) #시작 인덱스에는 알맞는 숫자
                #영단어 글자수 빈 자리에는 * 삽입
                an[sk+1:sk+len(key_list[i])] = '*' * (len(key_list[i])-1) 
                
       # print(an)
    # print(list(map(str,an)))
    answer = ''.join(an)
    return int(''.join(answer.split("*")))
