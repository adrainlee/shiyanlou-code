#!/usr/bin/env python3

num_list = [x for x in range(1,101) if x / 7 != 0]
for i in num_list:
    if '7' in str(i):
        continue
    else:
        print(i)
