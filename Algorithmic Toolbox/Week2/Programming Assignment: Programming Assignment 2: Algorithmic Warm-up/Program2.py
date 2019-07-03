# python3

def fibo(n):
    a = 0
    if n==0:
        return a
    b = 1
    if n==1:
        return b
    for i in range(2,n+1):
        c = (a+b)%10
        a = b
        b = c
            
    return c           
                

if __name__ == '__main__':
    n = int(input())  
    print(fibo(n))
     
