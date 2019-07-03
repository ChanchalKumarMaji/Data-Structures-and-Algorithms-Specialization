# python3

def solve(S):

    brackets = []
    for i in range(len(S)):
        if S[i]=='(' or S[i]==')' or S[i]=='{' or S[i]=='}' or S[i]=='[' or S[i]==']':
            brackets.append((S[i], i+1)) 
    #print(brackets) 
    
    stack = []
    for bracket in brackets:
        b, idx = bracket[0], bracket[1]
        if b=='(' or b=='{' or b=='[':
            stack.append(bracket) 
        elif b==')' or b=='}' or b==']':
            if len(stack)==0:
                return idx
            else:
                pre = stack[-1]
                pre_b, pre_idx = pre[0], pre[1]
                stack.pop()
                if b==')':
                    if pre_b!='(':
                        return idx
                elif b=='}':
                    if pre_b!='{':
                        return idx
                elif b==']':
                    if pre_b!='[': 
                        return idx
    if len(stack)==0:
        return "Success"
    else:
        return stack[0][1]                         
                                
             


if __name__ == '__main__':
    S = input()
    print(solve(S))  
        
            


    









                

