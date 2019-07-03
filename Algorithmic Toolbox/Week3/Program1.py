# python3

def solve(m):
    c_10 = m//10
    m = m%10
    c_5 = m//5
    m = m%5
    c_1 = m
    
    return c_10 + c_5 + c_1
    
if __name__ == '__main__':
    m = int(input())
    print(solve(m)) 
    
    
        
