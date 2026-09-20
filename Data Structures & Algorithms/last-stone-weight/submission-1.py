class Solution:
    def lastStoneWeight(self, stones) -> int:
        #sorting the array from high to low 
        stones = sorted(stones, reverse=True)
        #While the length is more than one index y to the first number 
        #and index y to the second number 
        #grab the difference from y and x 
        while len(stones) > 1:
            y = stones[0]
            x = stones[1]
            diff = y - x
            
            stones = stones[2:]
            if diff > 0:
                stones.append(diff)

            stones.sort(reverse=True)

        return stones[0] if stones else 0
   