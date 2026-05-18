class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        total, curr = gas[0], 0
        for i in range(1, len(gas)):
            total -= cost[i - 1]
            if total < 0:
                curr = i
                total = gas[i]
            else:
                total += gas[i]
        return curr