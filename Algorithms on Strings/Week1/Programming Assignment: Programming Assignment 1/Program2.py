# python3 

def find(text, trie): 
    res = []
    for i in range(len(text)): 
        curr = 0
        j = i
        present = False
 
        while True:
            p = curr
            for k in range(len(trie[curr][2])): 
                if trie[(trie[curr][2])[k]][0] == text[j]:
                    curr = (trie[curr][2])[k] 
                    present = trie[curr][1] 
                    j += 1
                    break
                    
            if present:
                res.append(i)
                break         
            
            if j>=len(text):
                break 
                
            if p == curr:
                break
                
    return res                 

def solve(text, patterns):
   
    node = ['#', False, []]    # key, end, list  
    trie = [node]
    counter = 0                # keeps track of the number of nodes 
    for pattern in patterns:
        curr = 0 
        for i in range(len(pattern)):
            c = pattern[i] 
            found = False 
            for j in range(len(trie[curr][2])):
                if trie[(trie[curr][2])[j]][0] == c:
                    curr = trie[curr][2][j] 
                    found = True 
                    break 
            if not found:
                counter += 1
                trie.append([c, False, []])
                trie[curr][2].append(counter) 
                curr = counter                
            if i == len(pattern)-1:
                trie[curr][1] = True                           
    
    #print(trie)
    
    for e in find(text, trie):
        print(e, end=' ')
    print()       
                     
                      

if __name__ == '__main__':
    text = input()
    n = int(input())
    patterns = []
    for n0 in range(n):
        pattern = input() 
        patterns.append(pattern) 
    solve(text, patterns)        
        
            


    









                

