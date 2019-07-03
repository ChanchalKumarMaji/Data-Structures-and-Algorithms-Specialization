# python3 

def lps(pattern):
    pattern = '#'+pattern  
    length = len(pattern)
    table = [0 for i in range(length)] 
    
    table[1] = 0
    
    for i in range(2, length):
        j = table[i-1]  
        while pattern[j+1] != pattern[i] and j>0:
            j = table[j]   
            
        if pattern[j+1] == pattern[i]:  
            table[i] = j+1 
            
    return table 
    

if __name__ == '__main__':
    pattern = input()
    text = input() 
    table = lps(pattern+'$'+text)
    
    for i in range(len(pattern)+2, len(table)):
        if table[i] == len(pattern):
            print(i-2*len(pattern)-1, end=" ") 
            
    print()           
    
