# python3

def solve(N):
    d = {}
    for N0 in range(N):
        l = input().split()
        if l[0] == 'add':
            d[l[1]] = l[2]
        elif l[0] == 'del':
            d.pop(l[1], None)
        elif l[0] == 'find':
            if l[1] in d.keys():
                print(d[l[1]])
            else:
                print('not found')     
            


if __name__ == '__main__':
    
    N = int(input())
    solve(N)   
        
            


    









                

