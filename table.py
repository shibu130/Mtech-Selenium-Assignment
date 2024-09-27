import numpy as np
a =  ['a','b'] 
b =  ['c','d'] 
c =  ['c','d'] 
#print(zip(a,b,c))

print([list(a) for a in zip(a,b,c)])