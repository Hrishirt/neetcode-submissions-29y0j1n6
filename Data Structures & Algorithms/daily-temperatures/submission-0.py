class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures): 
            while stack and temp > stack[-1][0]:
                popTemp,popIndex  = stack.pop() 
                output[popIndex] = (index - popIndex)
            stack.append([temp, index])
        return output