class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        hashmap = {')': '(', '}': '{', ']': '['}
        if len(s) % 2 != 0:
            return False
        for b in s:
            if b in hashmap: 
                if len(stack) != 0 and stack[-1] == hashmap[b]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(b)
        if len(stack) == 0:
            return True
        else:
            return False