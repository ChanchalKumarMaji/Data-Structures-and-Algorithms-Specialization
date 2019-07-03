# python3

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
        res[i] = (ans) / A[i][pivot]
        pivot -= 1            
    
    res = [str.format("{0:.6f}", e) for e in res]
    print(" ".join(res))
    
if __name__ == '__main__':
    n = int(input())  
    if n==0:
        print()
    else:    
        A = []
        for _ in range(n):
            a = [int(i) for i in input().split()]
            A.append(a)
        solve(A, n)    
    
