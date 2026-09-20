class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_nums = {}
        for index, n in enumerate(nums):
            num = target - n
            if num in my_nums:
                return [my_nums[num], index]
            my_nums[n] = index

                