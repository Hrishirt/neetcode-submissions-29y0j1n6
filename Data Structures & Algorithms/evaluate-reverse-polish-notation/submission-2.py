class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x == "+":
                stack.append(stack.pop() + stack.pop())
            elif x == "-":
                num1 = stack.pop()
                num2 = stack.pop() 
                stack.append(num2 - num1) 
            elif x == "/":
                num1 = stack.pop()
                num2 = stack.pop() 
                stack.append(int(num2 / num1))
            elif x == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(x))
        return stack.pop()