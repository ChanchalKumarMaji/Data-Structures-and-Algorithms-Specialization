# python3

n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()] 
l = int(input())
c = [int(i) for i in input().split()] 

dp = [[[0 for k in range(l+1)] for j in range(m+1)] for i in range(n+1)] 

for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(1, l+1):
            if a[i-1] == b[j-1] == c[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])  
print(dp[-1][-1][-1]) 





                

