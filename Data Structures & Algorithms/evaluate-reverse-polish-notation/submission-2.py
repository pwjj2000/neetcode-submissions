class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "-":
                stack.append(-stack.pop() + stack.pop())
            elif c == "/":
                denom = stack.pop()
                stack.append(int(float(stack.pop()) / denom))
            else:
                stack.append(int(c))
        return stack[0]