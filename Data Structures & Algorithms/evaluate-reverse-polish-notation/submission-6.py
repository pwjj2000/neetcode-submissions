class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                o2 = stack.pop()
                o1 = stack.pop() 
                stack.append(o1 + o2)
            elif token == "-":
                o2 = stack.pop()
                o1 = stack.pop() 
                stack.append(o1 - o2)
            elif token == "*":
                o2 = stack.pop()
                o1 = stack.pop() 
                stack.append(o1 * o2)
            elif token == "/":
                o2 = stack.pop()
                o1 = stack.pop() 
                stack.append(int(o1/o2))
            else:
                stack.append(int(token))
        return stack[0]
            
