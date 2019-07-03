# python3

def fibo(n, m):
    a = 0
    b = 1
    
    p = [a%m, b%m]
    
    while True:
        c = a + b
        a = b
        b = c
        p.append(c%m) 
        if p[-2]==0 and p[-1]==1:
            break
            
    p = p[:-2]        
    lenPeriod = len(p) 
    
    #print(p)
    #print(lenPeriod)
    
    return p[n%lenPeriod]        
      

if __name__ == '__main__':
    n, m = map(int, input().split())   
    print(fibo(n, m))
