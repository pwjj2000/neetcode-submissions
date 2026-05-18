class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        answer = []
        for c in digits:
            if not answer:
                answer = d[c]
            else:
                prev_len = len(answer)
                answer = answer * len(d[c])
                for i in range(len(answer)):
                    answer[i] += d[c][i // prev_len]
        return answer