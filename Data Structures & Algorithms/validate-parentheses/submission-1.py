class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            elif c == ')' and (len(stack) == 0 or stack.pop() != '('):
                return False
            elif c == ']' and (len(stack) == 0 or stack.pop() != '['):
                return False
            elif c == '}' and (len(stack) == 0 or stack.pop() != '{'):
                return False
        return len(stack) == 0
                