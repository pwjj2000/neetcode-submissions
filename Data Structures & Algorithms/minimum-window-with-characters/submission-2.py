class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tchars, schars = {}, {}
        shortest, shortest_length = "", len(s)
        same = 0
        for c in t:
            tchars[c] = 1 + tchars.get(c, 0)
        l = 0
        for r in range(len(s)):
            if s[r] in tchars:
                schars[s[r]] = 1 + schars.get(s[r], 0)
                if schars[s[r]] == tchars[s[r]]:
                    same += 1
            if same == len(tchars.keys()) and r - l + 1 <= shortest_length:
                shortest = s[l:r + 1]
                shortest_length = r - l + 1
            while l < len(s) and same == len(tchars.keys()):
                if s[l] not in tchars:
                    l += 1
                elif schars[s[l]] == tchars[s[l]]:
                    if r - l + 1 < shortest_length:
                        shortest = s[l:r + 1]
                        shortest_length = r - l + 1 
                    same -= 1
                    schars[s[l]] -= 1
                    l += 1
                else:
                    schars[s[l]] -= 1
                    l += 1
        return shortest
            

        
        
        