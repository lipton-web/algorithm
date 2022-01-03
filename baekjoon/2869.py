# a, b, v = map(int, input().split())

# print((v-a)//(a-b)+1)


a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1) 