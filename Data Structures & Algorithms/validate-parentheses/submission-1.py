class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            #get prefixes
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            #match with the drawn postfix
            else:
                #empty stack edge case for closed brackets
                if len(stack) == 0: return False
                #match the closing prefix to the appropriate postfix
                match c:
                    case ')': 
                        if stack[-1] != '(': return False
                        else: stack.pop()
                    case '}': 
                        if stack[-1] != '{': return False
                        else: stack.pop()
                    case ']': 
                        if stack[-1] != '[': return False
                        else: stack.pop()

        #if the are any remaining items, it is invalid
        if len(stack) > 0: return False                
        return True
                    