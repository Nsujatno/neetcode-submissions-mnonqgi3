class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            size = len(stack) - 1
            
            if s[i] == ')':
                if size < 0:
                    return False
                if stack[size] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if size < 0:
                    return False
                if stack[size] == '[':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if size < 0:
                    return False
                if stack[size] == '{':
                    stack.pop()
                else:
                    return False
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            print(stack)
        print("stack at the end: ", stack)
        if len(stack) == 0:
            return True
        else:
            return False