T = int(input())

for i in range(T):	
	H, W, N = map(int, input().split())

	floor = N%H #층수
	number=(N//H)+1 #호수
	
	if N % H == 0:
		number = N // H
		floor = H

	print(floor*100+number)


# 오답
# print(H,W,N)

# h = 30
# w = 50
# n = 72

	# if N <= H:
	# 	print(str(N)+"01")
	# else:
	# 	k=((N//H)+1) #호수
	# 	p=(N%H) #층수
	# 	print(str(p)+"0"+str(k))
