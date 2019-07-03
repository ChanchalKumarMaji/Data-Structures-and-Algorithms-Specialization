# python3

from collections import deque

def solve(S, n, process):
    
    q = deque([])
    
    res = [0 for i in range(n)]
     
    start = process[0][0]
    end = start+process[0][1]
       
    q.append((process[0][0], process[0][1], 0))  
    
    for i in range(1, n):
    
        s, e = process[i][0], process[i][1] 
        
        if s>=end:
            while len(q)!=0 and q[0][0]+q[0][1]<=s:
                end = start
                res[q[0][2]] = end  
                end += q[0][0]+q[0][1]  
                q.popleft() 
            
            q.append((process[i][0], process[i][1], i))
        
            start = end 
            end = start + q[0][1] 
            
        else:
            if len(q)<S:
                q.append((process[i][0], process[i][1], i)) 
            else:
                res[i] = -1         
        
    while len(q)!=0:
        res[q[0][2]] = q[0][0] 
        q.popleft()     
        
    #print(res)                         
                                
    return res         


if __name__ == '__main__':
    S, n = map(int, input().split())
    process = []
    for n0 in range(n):
        A, P = map(int, input().split())
        process.append((A, P)) 
    for e in solve(S, n, process):
        print(e)   
        
            


    









                

