#내가 푼 풀이 - 인터넷 찾아보니 n이 커지면 소요시간이 커진다는 단점 있음

n, k = map(int, input().split())
num = 0

print(n,k)
while n!=1:
  if n%k==0:
    n = n//k
  else:
    n = n-1
  num +=1
 
print(num)
