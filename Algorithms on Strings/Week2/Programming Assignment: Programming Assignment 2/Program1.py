# python3

def BWT(text):
    
    n = len(text) 
    text = text + text
     
    l = []
    for i in range(n): 
        l.append(text[i:i+n])
        
    l.sort()
    
    res = '' 
    for s in l:
        res += s[-1]      
            
    return res 
    
    
if __name__ == "__main__":

    text = input()
    print(BWT(text))     



               
