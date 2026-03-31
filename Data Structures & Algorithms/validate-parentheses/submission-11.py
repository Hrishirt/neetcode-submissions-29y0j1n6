class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {')': '(', '}': '{', ']': '['}
        if len(s) % 2 != 0:
            return False
        
        for x in s:
            print(x)
            if x in openToClose:
                print(x)
                if len(stack) != 0 and openToClose[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        
        if len(stack) == 0:
            return True
        else:
            return False