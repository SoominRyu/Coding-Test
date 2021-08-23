#내 풀이
n = input()
n = list(map(int,n))

i=0
num = 0

for i in n:
  if i<=1 or num<=1:
    num += i
  else:
    num *= i
    
print(num)


# 예시 풀이
n = input()

result = int(n[0])

for i in range(1, len(n)):
  num = int(n[i])
  if num<=1 or result<=1:
    result += num

  else:
    result *=num

print(result)
