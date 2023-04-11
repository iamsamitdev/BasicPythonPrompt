# Import from packages
# Import all the packages
from numberpackage import *
import numberpackage as np
from numberpackage import number as nb
from numberpackage import calcuate as ca

print(numberpackage.number.factorial(5))
print(numberpackage.number.fibonacci(100))
print(numberpackage.calcuate.plus(5, 6))

print(np.number.factorial(5))
print(np.number.fibonacci(100))
print(np.calcuate.plus(5, 6))

print(nb.factorial(5))
print(nb.fibonacci(100))
print(ca.plus(5, 6))
