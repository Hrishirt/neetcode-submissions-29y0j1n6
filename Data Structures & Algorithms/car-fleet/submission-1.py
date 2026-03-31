class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 
        posSpeed = [[p,s] for p,s in zip(position,speed)]
        for pos, speed in reversed(sorted(posSpeed)): 
            time = (target-pos)/ speed 
            stack.append(time)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)