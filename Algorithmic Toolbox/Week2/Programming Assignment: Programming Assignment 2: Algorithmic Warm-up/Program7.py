# python3

def fibo(n):
    a = 0
    if n == 0:
        return 0
    
    b = 1
    if n == 1:
        return 1
    
    p = [0, 1]
    while True:
        c = a + b
        a = b
        b = c
        p.append((c)%10)  
        if len(p)>59:
            break
    
    period = len(p)         
    
    #print(p)        
    #print(period)
    
    q = n//period
    r = n%period
    
    return (q*sum(p) + sum(p[:r+1]))%10 
     
def find(m, n):
    return (fibo(n) - fibo(m-1))%10            
    
if __name__ == '__main__':
    m, n = map(int, input().split())  
    print(find(m, n))  
