# num = 3
# # num = int(input())

# def sugerBag(input) :
# 	bag = 0
# 	while input >= 0 :
# 			if input % 5 == 0 :  # 5의 배수이면
# 					bag += (input / 5)  # 5로 나눈 몫을 구해야 정수가 됨
# 					# print(bag)
# 					return bag
# 			else :
# 				input -= 3  
# 				bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1

# 			if input < 2 :
# 				return -1  

# 	else :
# 			return -1


# result = sugerBag(num)
# print(result)



sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)



# print(num)

# a = 0
# while input >= 0 :
# 	input - 3
# 	print(input)
# 	a = a + 1
# print(a)




# def sugerNum(input) :
	# if input < 3 :
	# 	return -1

	# # elif input % 5 != 0 or input % 3 != 0 :
	# # 	return

	# elif input % 5 == 0:
	# 	return input/5

	# elif input % 5 != 0 :

		# a = 0
		# kg = input
		# while kg % 5 == 0 :
		# 	print("aa")
			# kg - 3
			# a += 1

			# return kg/5 + a

			# if kg-3 < 2 :
			# 	return -1



	
	

		# return input
	


# result = sugerNum(input)
# print(result)