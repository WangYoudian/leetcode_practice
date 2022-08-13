#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1:
            return False
        # n > 1
        if n <= k:
            return len(set(nums)) != n
        window = set(nums[:k])
        # n > k
        if len(window) < k:
            return True

        for i in range(k, n):
            if nums[i] in window:
                return True
            else:
                window.add(nums[i])
                window.remove(nums[i - k])
        return False

# @lc code=end

