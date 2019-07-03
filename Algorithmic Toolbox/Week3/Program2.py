# python3

def solve(W, arr):
    arr.sort(reverse = True)
    value = [e[0] for e in arr]
    weight = [e[1] for e in arr]
    if weight[0]>=W:
        return W*value[0]
    if sum(weight)<=W:
        return sum([v*w for v, w in zip(value, weight)])    
    res = 0
    s = 0
    for i in range(len(weight)):
        if s+weight[i]>W:
            break
        else:
            s += weight[i]
            res += weight[i]*value[i] 
    res += (W-s)*value[i]        
    
    return res    
    
if __name__ == '__main__':
    n, W = map(int, input().split())
    arr=[]
    for n0 in range(n):
        v, w = map(int, input().split())
        arr.append([v/w, w])
    print("%0.4f" %solve(W, arr))    
    
    
        
