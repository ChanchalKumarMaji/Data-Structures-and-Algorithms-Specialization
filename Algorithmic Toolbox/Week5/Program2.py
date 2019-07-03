# python3

def solve(n):
    dp = [[0, 0] for i in range(10**6 + 1)]
    dp[2][0], dp[2][1] = 1, 1
    dp[3][0], dp[3][1] = 1, 1
    for i in range(4, n+1):
    
        b0, c0 = -1, -1
        a0, a1 = dp[i-1][0], i-1
        if i%2 == 0:
            b0, b1 = dp[i//2][0], i//2
        if i%3 == 0:
            c0, c1 = dp[i//3][0], i//3 
            
        if b0==-1 and c0==-1:
            dp[i][0], dp[i][1] = a0 + 1, a1
        elif b0==-1 and c0!=-1:
            if a0<=c0:
                k = a1
            else:
                k = c1    
            dp[i][0], dp[i][1] = min(a0, c0) + 1, k
        elif c0==-1 and b0!=-1:
            if a0<=b0:
                k = a1
            else:
                k = b1    
            dp[i][0], dp[i][1] = min(a0, b0) + 1, k 
        elif b0!=-1 and c0!=-1:                               
            if a0<=b0 and a0<=c0:
                k = a1
            elif b0<=a0 and b0<=c0:
                k = b1
            elif c0<=a0 and c0<=b0:
                k = c1         
            dp[i][0], dp[i][1] = min(a0, b0, c0) + 1, k 

    print(dp[n][0]) 
    res = dp[:n+1]
    l = [] 
    i = n
    while i>1:
        l.append(i)
        i = res[i][1]
    l.append(1)
    l = l[::-1]
    print(" ".join([str(i) for i in l]))    
                   
         
if __name__ == '__main__':
    n = int(input())
    solve(n)     
    
    
        
