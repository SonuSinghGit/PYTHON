import modul1
print(modul1.sum(12,34))

import  modul1
print(modul1.mul(12,10))
#ANOTHER WAY
from modul1 import sum
print(sum(12,23))

from modul1 import *
print(mul(12,12))
print(sum(10,10 ))

#OR MAKING ELIAAS
import modul1 as m
print(m.mul(2,3))
print(m.sum(4,4))