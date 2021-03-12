###########################
# Calculation of SUM (pij) for solid state physics

summa = 0

lst = [-1,0,1]
# for bcc
for i in range(-10,11):
    for j in range(-10,11):
        for k in range(-10,11):

            # a1 = (1/2, 1/2,   0)
            # a2 = (0,   1/2, 1/2)
            # a3 = (1/2,   0, 1/2)

            x =  i/2.0  +  j/2.0 -  k/2.0
            y =  i/2.0  -  j/2.0 +  k/2.0
            z = -i/2.0  +  j/2.0 +  k/2.0

            x *= 2/3**0.5
            y *= 2/3**0.5
            z *= 2/3**0.5
            
            if not ( (i == 0) and (j == 0) and (k == 0) ):
                r = (x*x + y*y + z*z)**0.5

                summa += 1/r**12
            


print(summa)
