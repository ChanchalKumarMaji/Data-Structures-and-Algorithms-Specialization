# python3

def solve(n, v):
    #if sum(v) % 3 != 0:
    #    return False
    res = []
    values = []
    s = sum(v)//3 
    for i in range(2**n):
        bit = [0 for i in range(n)]           
        k = i
        p = n-1
        while k!=0:
            bit[p] = (k%2)
            k = k//2
            p -= 1
               
        #print(bit)
        
        val = [a*b for a, b in zip(v, bit)] 
        #print(val)
        
        if sum(val) == s:
           res.append(bit)
           values.append(i) 
    #print(res) 
    #print(values)
    if len(res)<3:
        return False
    for i in range(len(values)-2):
        for j in range(i+1, len(values)-1):
            for k in range(i+2, len(values)):
                a = values[i]
                b = values[j]
                c = values[k]
                if a^b^c == (2**n-1):
                    return True
    return False                       
              
         
if __name__ == '__main__':
    n = int(input())
    v = [int(i) for i in input().split()] 
    if solve(n, v):
        print("1")
    else:
        print("0")    
        
