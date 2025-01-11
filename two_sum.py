from typing import List

'''My firts Solution'''
# class Solution:
#   def twoSum(self, nums: List[int], target: int) -> List[int]:
#     i = 0
#     j = 0

#     while i < len(nums):
      
#       while j < len(nums):
#         if nums[i] + nums[j] == target and i != j:
#           return [i, j]
#         j += 1
      
#       i += 1
#       j = 0

'''My second solution'''
# class Solution:
#   def twoSum(self, nums: List[int], target: int) -> List[int]:
#     self.nums = nums
#     self.target = target
#     self.recursive(0, 0,)

#     return self.sol
  
#   def recursive(self, v_act_index, c_index):
    
#     if c_index < len(self.nums) and self.nums[v_act_index] + self.nums[c_index] == self.target and v_act_index != c_index :
#       self.sol = [v_act_index, c_index]
#       return
    
#     if c_index >= len(self.nums):
#       self.recursive((v_act_index + 1), 0 )
#     else:
#       self.recursive( v_act_index, (c_index + 1))

'''Optimal solution'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        processMap = {}

        for i, v in enumerate(nums):
            if target-v in processMap:
                return [processMap[target-v], i]
            
            processMap[v] = i

sol = Solution()
print(sol.twoSum([3,1,3], 6))

# ¿Que necesito saber?
# index actual, self.nums, target