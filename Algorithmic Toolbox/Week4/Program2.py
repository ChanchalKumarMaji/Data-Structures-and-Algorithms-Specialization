# python3

import collections

def solve(n, a):
    d = collections.defaultdict(int) 
    for i in range(n):
        d[a[i]] += 1
    l = list(d.values())
    k = n//2
    for e in l:
        if e>k:
            return True
    return False                  
                     

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()] 
    if solve(n, a):
        print("1")
    else:
        print("0")      
    
    
        
