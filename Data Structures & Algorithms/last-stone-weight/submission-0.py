class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones = sorted(stones, reverse=True)

        while len(stones) > 1:
            y = stones[0]
            x = stones[1]
            diff = y - x

            stones = stones[2:]
            if diff > 0:
                stones.append(diff)

            stones.sort(reverse=True)

        return stones[0] if stones else 0
   