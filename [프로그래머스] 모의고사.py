def solution(answers):
    answer = []
    # student = {1:[1,2,3,4,5], 2:[2,1,2,3,2,4,5], 3:[3,3,1,1,2,2,4,4,5,5]}
    student = [[1,2,3,4,5],[2,1,2,3,2,4,5],[3,3,1,1,2,2,4,4,5,5]]
    
    result = [0,0,0]
    anum = len(answers)
    
    for i in range(anum):
        #1번 수포자
        if answers[i%anum] == student[0][i%len(student[0])]:
            result[0] += 1
                
        #2번 수포자
        if answers[i%anum] == student[1][i%len(student[1])]:
                # print("answer",answers[i%anum])
                # print("su2",student[1][su2%len(student[1])])
            result[1] += 1
                
          #3번 수포자

        if answers[i%anum] == student[2][i%len(student[2])]:
            result[2] += 1
    
    
    # print(result)
    # answer = [result.index(max(result))+1]
    
    for i in range(3):
        if result[i] == max(result):
            answer.append(i+1)
    
    
    
    # print(student[1])
    return answer
