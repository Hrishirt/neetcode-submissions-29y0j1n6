class Solution:
    def isValid(self, s: str) -> bool:
        openToclose = {')': '(', '}': '{', ']': '['}
        stack = []

        if len(s) % 2 != 0:
            return False

        for x in s: 
            if x in openToclose:
                if len(stack) != 0 and stack[-1] == openToclose[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        
        if len(stack) == 0:
            return True
        else:
            return False