# python3 

def SortCharacters(S):

    order = [0 for i in range(len(S))] 
    count = [0 for i in range(256)] 
    
    for i in range(len(S)):
        count[ord(S[i])] += 1
        
    for j in range(1, 256):
        count[j] += count[j-1]
        
    for i in range(len(S)-1, -1, -1):
        c = ord(S[i]) 
        count[c] -= 1 
        order[count[c]] = i
        
    return order             
        

def ComputeCharClasses(S, order):
    
    Class = [0 for i in range(len(S))] 
    Class[order[0]] = 0
    
    for i in range(1, len(S)):
        if S[order[i]] != S[order[i-1]]:
            Class[order[i]] = Class[order[i-1]] + 1
        else:
            Class[order[i]] = Class[order[i-1]] 
            
    return Class 
    
    
def SortDoubled(S, L, order, Class):

    count = [0 for i in range(len(S))] 
    newOrder = [0 for i in range(len(S))] 
    
    for i in range(len(S)): 
        count[Class[i]] += 1
        
    for j in range(1, len(S)):
        count[j] += count[j-1] 
        
    for i in range(len(S)-1, -1, -1):
        start = (order[i] - L + len(S)) % len(S)
        cl = Class[start]
        count[cl] -= 1
        newOrder[count[cl]] = start
        
    return newOrder 
    
  
def UpdateClasses(newOrder, Class, L):
    
    n = len(newOrder)
    newClass = [0 for i in range(n)] 
    
    newClass[newOrder[0]] = 0
    
    for i in range(1, n):
        cur = newOrder[i] 
        prev = newOrder[i-1]
        mid = cur + L
        midPrev = (prev + L) % n 
        if Class[cur] != Class[prev] or Class[mid] != Class[midPrev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev] 
            
    return newClass                 
                         
    
    
    
    
                   



    

if __name__ == '__main__':
    
    S = input()
    
    order = SortCharacters(S)
    Class = ComputeCharClasses(S, order) 
    L = 1 
    
    while L < len(S):
        order = SortDoubled(S, L, order, Class) 
        Class = UpdateClasses(order, Class, L)
        L = 2*L
        
    for e in order:
        print(e, end = " ")
    print() 
    
    
    
              
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
              
