#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            nums[p] = nums[i]
            p += 1
        return p

# @lc code=end

