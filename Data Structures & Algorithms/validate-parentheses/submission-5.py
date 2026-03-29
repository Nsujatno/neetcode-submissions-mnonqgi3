class Solution:
    def isValid(self, s: str) -> bool:
        # store in stack, for every opening parenthesis push to stack. for closing parenthesis
        # check if that corresponding open is at the top of the stack
        stack = []
        for char in s:
            # print(char)
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if char == ")":
                    if top != "(":
                        return False
                if char == "}":
                    if top != "{":
                        return False
                if char == "]":
                    if top != "[":
                        return False
        
        if len(stack) != 0:
            return False
        return True