# python3

def solve(a, b):
    d = {}
    for i in range(len(a)):
        d[a[i]] = i
    res = []    
    for e in b:
        if e in d:
            res.append(d[e])
        else:
            res.append(-1)
            
    print(" ".join([str(i) for i in res]))          
                     

if __name__ == '__main__':
    na = [int(i) for i in input().split()]
    n = na[0]
    a = na[1:]
    kb = [int(i) for i in input().split()]
    k = kb[0]
    b = kb[1:] 
    solve(a, b) 
    
    
        
