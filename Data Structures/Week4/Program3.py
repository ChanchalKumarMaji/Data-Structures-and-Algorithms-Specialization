# python3         

def solve(P, T):
    p = 1000000007
    x = 256
    check = 0
    for i in range(len(P)): 
        check += (ord(P[i])*(pow(x, (len(P)-i-1), p)))%p 
    check = check%p
    
    slide = 0
    for i in range(len(P)):
        slide += (ord(T[i])*(pow(x, (len(P)-i-1), p)))%p 
    slide = slide%p
    
    j = len(P)
    if slide==check and P==T[0:j]: 
        print('0', end=" ") 
    
    for i in range(1, len(T)-len(P)+1):
        j += 1
        slide = (slide-((ord(T[i-1])*(pow(x, (len(P)-1), p)))%p))*x + (ord(T[j-1])) 
        slide = slide%p   
        if slide==check and P==T[i:j]: 
            print(i, end=" ")
    print()                        
            


if __name__ == '__main__':
    P = input()
    T = input()
    solve(P, T) 
       
        
            


    









                

