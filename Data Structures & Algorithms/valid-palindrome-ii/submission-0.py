class Solution:
    def validPalindrome(self, s: str) -> bool:
        delete = False
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif not delete:
                delete = True
                if l + 1 < r and s[l+1] == s[r]:
                    l += 1
                elif l < r - 1 and s[l] == s[r-1]:
                    r -= 1
                elif l + 1 < r:
                    l += 1
                else:
                    r -= 1
            else:
                return False
        return True