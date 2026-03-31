class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens: 
            if char == "+":
                added = stack.pop() + stack.pop() 
                stack.append(added)
                print(stack)
            elif char == "*":
                mult = stack.pop() * stack.pop()
                stack.append(mult)
                print(stack)
            elif char == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                sub = num2 - num1
                stack.append(sub)
                print(stack)
            elif char == "/":
                num1 = stack.pop()
                num2 = stack.pop() 
                div = num2 / num1
                stack.append(int(div))
            else:
                stack.append(int(char))
                print(stack)
        return stack.pop()