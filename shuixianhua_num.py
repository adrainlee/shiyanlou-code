#!/usr/bin/env python3

for x in range(100,1000):
    i = divmod(x,100)[0]
    j = divmod(divmod(x,100)[1],10)[0]
    k =divmod(divmod(x,100)[1],10)[1] 
    if x == i ** 3 + j ** 3 + k ** 3:
        print(x)
    
