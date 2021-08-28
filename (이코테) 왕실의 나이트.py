#num = 8, 8
arr = [[0 for r in range(8)] for c in range(8)]
col = ['a','b','c','d','e','f','g','h']
move = input()
count = 0


steps = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

for i in range(8):
  for j in range(8):
    arr[i][j] = col[j] + str(i+1)
    if(move == arr[i][j]):
      for s in steps:
        move_i = i+s[0]
        move_j = j+s[1]
        if move_i >=1 and move_j >=1 and move_i<=8 and move_j<=8:
          count+=1

print(count)

