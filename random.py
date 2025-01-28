import random

for i in range(100):
    c = random.randit(0,10)
    print(c)

import random

for i in range(100):
    c = random.randrange(11,100,2)
    print(c)


import random

c = random.randint(0,100)
if c % 2 ==0:
    print(c,"je parne")
else:
    print(c,"je neparne")
    

import random

x = random.randint(-20,30)
print("dnes je", x, "stupnov")


x = int(input("ake cislo si od 1 az 10 myslim:"))

import random
c = random.randint(1,10)
print("ja si myslim cislo", c )
if x == c:
    print("woow vyhral si")
else:
    print("blbe, prehral si")
