# 1. Two Sum
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9

# Output: [0,1]

# Explanation:

# The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.

# Example 2:

# Input: nums = [3,2,4], target = 6

# Output: [1,2]

# Explanation:

# The sum of nums[1] and nums[2] is 2 + 4 = 6, which equals the target. Therefore, the indices [1, 2] are returned.

# Example 3:

# Input: nums = [3,3], target = 6

# Output: [0,1]

# Explanation:

# The sum of nums[0] and nums[1] is 3 + 3 = 6, which equals the target. Therefore, the indices [0, 1] are returned.

 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



    #             or 
    #             class Solution:
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     seen = {}  # number → its index

    #     for i in range(len(nums)):
    #         needed = target - nums[i]
    #         if needed in seen:
    #             return [seen[needed], i]
    #         seen[nums[i]] = i
