dias = int(input())

a = dias // 365
a1 = dias % 365

m = a1 // 30
m1 = a1 % 30

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(m1))