class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join([c.lower() for c in s if c.isalnum()])
        print(string)
        i, j = 0, len(string) - 1
        while i <= j and string[i] == string[j]:
            i += 1
            j -= 1
        return i >= j
            
        