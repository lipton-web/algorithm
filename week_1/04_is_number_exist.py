input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
  # 이 부분을 채워보세요!
		for element in array: 	# array의 길이만큼 아래 연산 실행
			if number == element: 	# 비교연산 1번 실행
				return True 	# N * 1 = N 만큼

		# 비교했는데도 발견하지 못하면 false

		return False


result = is_number_exist(3, input)
print(result)