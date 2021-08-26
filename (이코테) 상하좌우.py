#내가 푼 풀이
n = int(input())
a = input().split() 
#굳이 a = list(input().split())으로 안 써도 됨

#현재 위치
x = 1
y = 1

for i in a:
  #n*n 벗어날 수 없음, y=1인 경우 왼쪽 이동 불가
  if i =="L" and y!=1: 
    y-=1
  elif i=="R" and y!=n:
    y+=1
  elif i=="U" and x!=1:
    x-=1
  elif i=="D" and x!=n:
    x+=1

print(x,y)


#답지 풀이
n = int(input())
x, y = 1, 1
#이동 계획 입력 받음
a = input().split()

#L R U D 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for i in a:
  #이동 후 좌표 구하기
  for j in range(len(move)):
   if i == move[j]:
     nx = x + dx[j]
     ny = y + dy[j]
  
  #공간 벗어나는 경우
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  #이동
  x, y = nx, ny

print(x, y)
