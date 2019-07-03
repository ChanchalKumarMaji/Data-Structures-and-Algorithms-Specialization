# python3

def solve(W, w):
    w.sort()
    dp = [[0 for j in range(W+1)] for i in range(len(w))]
    for j in range(1, W+1):
        if j >= w[0]:
            dp[0][j] = w[0] 
    for i in range(1, len(w)):
        for j in range(1, W+1):
            if j >= w[i]:
                dp[i][j] = max(dp[i-1][j], w[i] + dp[i-1][j-w[i]])                        
            else:
                dp[i][j] = dp[i-1][j]
    #print(dp)            
    print(dp[-1][-1])            
                
         
if __name__ == '__main__':
    W, n = map(int, input().split())
    w = [int(i) for i in input().split()]
    solve(W, w)     
    
    
        
