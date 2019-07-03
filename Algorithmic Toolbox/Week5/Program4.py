# python3

n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()] 

dp = [[0 for j in range(m+1)] for i in range(n+1)] 

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 
print(dp[-1][-1]) 





                

