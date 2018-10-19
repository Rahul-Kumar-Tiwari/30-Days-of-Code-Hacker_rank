import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    cons = 0
    max_c = 0
    while n>0 :
        remainder = n%2
        if remainder == 1:
            cons += 1
            if cons > max_c:
                max_c = cons
        else:
            cons = 0
        n = n//2
        
    print(max_c)
    
