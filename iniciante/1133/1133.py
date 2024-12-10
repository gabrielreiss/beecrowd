x = int(input())
y = int(input())

aux = 0

if y < x:
    aux = x
    x = y
    y = aux

for i in range(x+1,y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)