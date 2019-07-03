# python3

def solve(a, b):
    a.sort()
    b.sort()
    res = sum([i*j for i, j in zip(a, b)])
    return res


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()] 
    print(solve(a, b))   
    
    
        
