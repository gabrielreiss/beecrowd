n = 0
pos = 0

for i in range(0,100):
    x = int(input())
    if x > n:
        n = x
        pos = i + 1

print(n)
print(pos)