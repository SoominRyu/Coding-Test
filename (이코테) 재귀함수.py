
###
def recursive_function():
	print('재귀함수 호출')
	recursive_function()

recursive_function()

#오류메시지 발생할 수 있음 - 깊이 제한 있음

# 종료 조건을 포함한 재귀 함수 예제
def recursive_function(i):
	#100번째 호출을 했을 때 종료되도록 종료 조건 명시
	if i == 100:
	print(i, '번째 재귀함수에서', +i+1, '번째 재귀함수를 호출')
	recursive_function(i+1)
	print(i, '번째 재귀함수 종료')

recursive_function(1)

