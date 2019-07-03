# python3

def solve(n):
    dp = [0]*1000 
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 1
    dp[4] = 1
    for i in range(5, n+1):
        dp[i] = 1 + min(dp[i-1], dp[i-3], dp[i-4])
    print(dp[n])                    
                     

if __name__ == '__main__':
    n = int(input())
    solve(n)     
    
    
        
