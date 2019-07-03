# python3

def hash(S, m): 
    res = 0
    p = 1000000007
    x = 263
    for i in range(len(S)):
        res += ((ord(S[i]))*(x**i))%p
    return (res%p)%m         

def solve(m, N):
    d = {}
    for N0 in range(N):
        l = input().split() 
        if l[0] == 'add':
            s = l[1]
            h = hash(s, m)
            if h not in d:
                d[h] = []
                d[h].append(s) 
            else:
                if s not in d[h]:
                    d[h].append(s)
                
        elif l[0] == 'del':
            s = l[1]
            h = hash(s, m)
            if h in d:
                if s in d[h]:
                    d[h].remove(s) 
            
        elif l[0] == 'find':
            s = l[1]
            h = hash(s, m)
            if h in d:
                if s in d[h]:
                    print("yes")
                else:
                    print("no")     
            else:
                print("no")        
        
        elif l[0] == 'check': 
            i = int(l[1])
            if i in d:
                for e in d[i][::-1]:
                    print(e, end=" ")
                print() 
            else:
                print()
        #print(d)         
         
            


if __name__ == '__main__':
    m = int(input())
    N = int(input())
    solve(m, N)
       
        
            


    









                

