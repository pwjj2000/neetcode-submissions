class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num2) < len(num1):
            return self.multiply(num2, num1)
        def add(lst, string):
            carry, index = 0, len(lst) - 1
            for i in range(len(string) - 1, -1, -1):
                total = int(string[i]) + int(lst[index]) + carry
                lst[index] = str(total % 10)
                carry = total // 10
                index -= 1
            while carry > 0:
                total = int(lst[index]) + carry
                lst[index] = str(total % 10)
                carry = total // 10
                index -= 1
            return lst
        answer = ["0"] * (len(num1) + len(num2))
        
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            s = "0" * (len(num1) - 1 - i)
            for j in range(len(num2) - 1, -1, -1):
                total = int(num1[i]) * int(num2[j]) + carry
                s = str(total % 10) + s
                carry = total // 10
            if carry > 0:
                s = str(carry) + s
            answer = add(answer, s)
        index = 0
        while index < len(answer) and answer[index] == '0':
            index += 1
        return ''.join(answer[index:]) if index < len(answer) else '0'
        