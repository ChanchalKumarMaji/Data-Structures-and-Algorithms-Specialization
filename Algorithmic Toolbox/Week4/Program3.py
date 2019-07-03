# python3

import collections

def solve(n, a):
    a.sort()
    print(" ".join([str(i) for i in a]))                
                     

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()] 
    solve(n, a)     
    
    
        
