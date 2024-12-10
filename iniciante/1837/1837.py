n = input().split()
for i in range(0,len(n)):
    n[i] = int(n[i])

if n[1] > 0:
    q = n[0]//n[1]
    r = n[0] % n[1]
else:
    q = -(n[0]//(-n[1]))
    r = n[0] % (-n[1])

print(q,r)