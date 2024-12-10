s = int(input())

#s = 140153

h = s // 3600
h1 = s % 3600

m = h1 // 60
m1 = h1 % 60

print('{}:{}:{}'.format(h,m,m1))