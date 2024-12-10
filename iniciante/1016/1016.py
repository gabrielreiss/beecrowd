# essas duas linhas já resolvem
km = int(input())
#print('{} minutos'.format(km*2))



vx = 60
vy = 90

#1 km -> 2 min

#km = vy* t - vx * t
#km = t*(vy - vx)
t = (vy - vx)/km
t *=60
print('{:.0f} minutos'.format(t))
