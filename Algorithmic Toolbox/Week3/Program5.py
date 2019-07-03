# python3

import math

def solve(n):
    k = ((math.sqrt(1 + 8*n)) -1)/2
    k = int(k)
    print(k)
    s = 0
    for i in range(k-1):
        print(i+1, end=" ")
        s += i+1
    print(n-s)       

if __name__ == '__main__':
    n = int(input())
    solve(n) 
    
    
        
