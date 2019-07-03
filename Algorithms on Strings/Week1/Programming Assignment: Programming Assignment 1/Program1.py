# python3 

def solve(patterns):
   
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
    
    for i in range(len(trie)): 
        u = i
        for v in trie[u][2]:
            print(str(u)+'->'+str(v)+':'+str(trie[v][0])) 
                      


if __name__ == '__main__':
    n = int(input())
    patterns = []
    for n0 in range(n):
        pattern = input() 
        patterns.append(pattern) 
    solve(patterns)        
        
            


    









                

