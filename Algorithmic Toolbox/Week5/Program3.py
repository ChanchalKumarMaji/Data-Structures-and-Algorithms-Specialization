# python3

def solve(s1, s2):
    l1 = [None] + list(s1)
    m = len(l1)
    l2 = [None] + list(s2)
    n = len(l2)
    dp = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        dp[0][i] = i
    for i in range(m):
        dp[i][0] = i
        
    for i in range(1, m):
        for j in range(1, n):
            if l1[i] == l2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    print(dp[m-1][n-1])                          
    
         
if __name__ == '__main__':
    s1 = input()
    s2 = input()
    solve(s1, s2)     
    
    
        
