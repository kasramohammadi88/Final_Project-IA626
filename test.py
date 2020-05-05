import numpy as np  
from decimal import *

##getcontext().prec = 3
##a = getcontext()
##setcontext(a)

mealPrice = Decimal(str(4.98)).quantize(Decimal('.001'))
print(mealPrice)
print(type(mealPrice))
##print(x,y,step)

#a = np.arange(x,y,step)
#print(a)
#a = tuple(a)
#print(a)

##a = list(a)
##print(a)