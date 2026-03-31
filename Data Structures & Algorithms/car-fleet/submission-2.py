class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pospeed = [(p,s) for p,s in zip(position, speed)]
        stack = []
        for p,s in reversed(sorted(pospeed)):
            time = ((target - p) / s)
            stack.append(time)
            print(stack)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)