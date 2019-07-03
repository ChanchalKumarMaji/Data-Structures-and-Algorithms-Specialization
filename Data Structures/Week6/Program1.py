# python3 

import sys
sys.setrecursionlimit(10**6)

def solve(nodes):
    #print(nodes) 
    
    def inOrder(node):
        if node == -1:
            return
        inOrder(nodes[node][1])     
        print(nodes[node][0], end=" ")     
        inOrder(nodes[node][2])
    
    inOrder(0)          
    print() 
    
    def preOrder(node):
        if node == -1:
            return
        print(nodes[node][0], end=" ")     
        preOrder(nodes[node][1])
        preOrder(nodes[node][2])
        
    preOrder(0)
    print()
    
    def postOrder(node):
        if node == -1:
            return 
        postOrder(nodes[node][1])
        postOrder(nodes[node][2])
        print(nodes[node][0], end=" ")
        
    postOrder(0)
    print()                                  
            


if __name__ == '__main__':
    n = int(input()) 
    nodes = []
    for n0 in range(n):
        node = [int(i) for i in input().split()] 
        nodes.append(node)
    solve(nodes)   
        
            


    









                

