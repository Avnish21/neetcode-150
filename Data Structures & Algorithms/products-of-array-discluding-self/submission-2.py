import math
class Solution:
    def mnz(self, nums: List[int]):
        result = 1
        for n in nums:
            if n:
                result *= n
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums == [0] * len(nums):
            return nums
        product = math.prod(nums)
        nzproduct = self.mnz(nums)
        result = []
        for i in range(len(nums)):
            if not nums[i] and nums.count(0) > 1:
                result.append(0)
            elif not nums[i] and nums.count(0) == 1:
                result.append(nzproduct)
            else:
                result.append(product // nums[i])
        return result
        