from math import factorial

x = 20

r = x * 3.1415 / 180

c = 0

taylor = 0
while c <=5:
   taylor = taylor + (((-1) **c) * (r**(c*2))/ factorial(2*c))
   c +=1

print(f"{taylor:.3f}")