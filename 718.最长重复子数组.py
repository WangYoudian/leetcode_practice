#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
# 类似于最长公共子串问题 - 公共的，意味子数组连续

# @lc code=start
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            if nums1[0] == nums2[0]:
                return 1
            else:
                return 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans


# @lc code=end


if __name__ == '__main__':
    solution = Solution()
    A = [0, 0, 0, 0, 0]
    B = [0, 0, 0, 0, 0]
    print(solution.findLength(A, B))
