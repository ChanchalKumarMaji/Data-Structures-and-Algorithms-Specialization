# python3

from itertools import combinations
import math

def check(A, m, res):
    for e in A:
        a = 0
        for i in range(m):
            a += e[i]*res[i]
        if a+0.001 < e[-1]:
            return False    
    return True        

def row_op(r1, r2):
    r = [0 for i in range(len(r1))]
    for i in range(len(r1)):
        r[i] = r1[i] + r2[i]
    return r

def solve(A, n):
    pivot = 0
    for i in range(n):
        if A[i][pivot] == 0:
            for j in range(i+1, n):
                A[i] = row_op(A[i], A[j])
        if A[i][pivot] != 0:        
            A[i] = [e/A[i][pivot] for e in A[i]]
            for j in range(i+1, n):
                A[j] = row_op(A[j], [-e*A[j][pivot] for e in A[i]])
        pivot += 1     
    #print(A)                        
    
    pivot = n-1
    res = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        ans = A[i][n]
        for j in range(n-1, pivot, -1):
            ans -= A[i][j]*res[j] 
        if A[i][pivot] != 0:    
            res[i] = ans / A[i][pivot]
        else:
            return -1      
        pivot -= 1            
    
    return res
    
if __name__ == '__main__':
    n, m = map(int, input().split())  
    A = []
    for _ in range(n):
        a = [-int(i) for i in input().split()]
        A.append(a)
    b = [-int(i) for i in input().split()]
    for i in range(n):
        A[i].append(b[i]) 
    for i in range(m):
        a = [0 for i in range(m+1)]
        a[i] = 1
        A.append(a)   
    A.append([-1 for i in range(m)]+[-10**9])     
    p = [int(i) for i in input().split()]        
    
    #print(A)
    
    subsets = list(combinations(A, m))
    combs = []
    for subset in subsets:
        res = solve(list(subset), m)
        if res != -1 and check(A, m, res):
            a = 0
            for e1, e2 in zip(res, p):
                a += e1*e2
            res.append(a)
            combs.append(res)
    #print(combs)
    if len(combs) == 0:
        print("No solution")    
    else:
        l, a = combs[0][:-1], combs[0][-1]    
        
        for comb in combs:
            if a < comb[-1]:
                l, a = comb[:-1], comb[-1]
        
        if sum(l)+0.001 >= 10**9:
            print("Infinity")
        else:        
            l = [str.format("{0:.15f}", e) for e in l]  
            print("Bounded solution")      
            print(" ".join(l))    
    
