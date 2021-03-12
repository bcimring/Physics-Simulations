import random
nci = 0
nsq = 0

for i in range(10000000):
    x = random.randint(-50000, 50000)
    y = random.randint(-50000, 50000)

    if ( (x*x + y*y) <= 50000**2 ):
        nci += 1
    else:
        nsq += 1

print(4*nci/(nci+ nsq))
