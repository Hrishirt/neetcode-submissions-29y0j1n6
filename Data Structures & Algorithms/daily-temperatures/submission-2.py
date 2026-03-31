class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        output = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]: 
                popTemp, popIndex = stack.pop() 
                output[popIndex] = index - popIndex
            stack.append([temp, index])
        return output