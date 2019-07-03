# python3

def solve(arr):
    arr.sort()
    m = []
    while arr:
        a = arr[0][0]
        b = arr[0][1]
        arr.remove(arr[0])
        l = []
        for i in range(len(arr)):
            _a = arr[i][0]
            _b = arr[i][1]
            if max(a, _a)<=min(b, _b):
                l.append(arr[i])
                a = max(a, _a)
                b = min(b, _b) 
        for e in l:
            arr.remove(e)        
        m.append(b)      

    print(len(m))
    for e in m:
        print(e, end=" ")
    print()    

if __name__ == '__main__':
    n = int(input())
    arr = []
    for n0 in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])
    solve(arr)   
    
    
        
