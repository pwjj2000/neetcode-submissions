class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp, ll = "", 0
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                print(l, r)
                if r-l+1 > ll:
                    ll, lp = r-l+1, s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > ll:
                    ll, lp = r-l+1, s[l:r+1]
                l -= 1
                r += 1
        return lp

            
