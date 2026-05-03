class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #     else:
        #         return True
        # return False
        new_nums = list(set(nums))
        if len(new_nums) != len(nums):
            return True
        return False