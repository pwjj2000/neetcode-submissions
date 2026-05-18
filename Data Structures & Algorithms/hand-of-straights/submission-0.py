class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        if len(hand) % groupSize != 0:
            return False
        count, groups = {}, len(hand) // groupSize
        for h in hand:
            count[h] = count.get(h, 0) + 1
        for _ in range(groups):
            lowest = min(count.keys())
            for i in range(lowest, lowest + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
        return True
        

