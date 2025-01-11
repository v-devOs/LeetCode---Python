from typing import List


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    i = 0
    j = 0

    while i < len(nums):
      
      while j < len(nums):
        if nums[i] + nums[j] == target and i != j:
          return [i, j]
        j += 1
      
      i += 1
      j = 0

sol = Solution()
print(sol.twoSum([3,2,4], 6))

