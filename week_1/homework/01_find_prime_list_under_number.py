input = 20

# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는
# 반드시 N의 제곱근 이하
def find_prime_list_under_number(number):
	# 이 부분을 채워보세요!
	prime_list = []
	for n in range(2, number + 1): # n <- 2 ~ number+1,  n의 범위 : 2부터 number까지
		# n이 20 이라고 한다면
		# i 를 2 3
		# 2 ~ n - 1 중에서 소수인 친구들만
		# 소수 찾기
		for i in prime_list: # i의 범위: 2부터 n-1까의 소수
			if n % i == 0 and i * i <= n:
				break # 0으로 나누어 지면 소수 아님. 다시 반복
		else:
			prime_list.append(n) # 나누어 떨어지지 않으면 소수

	return prime_list



result = find_prime_list_under_number(input)
print(result)