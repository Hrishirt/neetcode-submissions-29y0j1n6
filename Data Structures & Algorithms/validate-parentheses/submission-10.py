class Solution:
    def isValid(self, s: str) -> bool:
        openToclose = {')': '(', '}': '{', ']': '['}
        stack = []

        if len(s) % 2 != 0:
            return False

        for par in s: 
            if par in openToclose:
                if len(stack) != 0 and openToclose[par] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
                print(stack)
        if len(stack) == 0:
            return True
        else:
            return False