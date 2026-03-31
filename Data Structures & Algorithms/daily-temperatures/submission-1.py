class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures): 
            while len(stack) > 0 and temperature > stack[-1][0]:
                popTemp, popIndex = stack.pop()
                output[popIndex] = index - popIndex
            stack.append([temperature, index])
        return output