#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        d = []
        for key, value in c.items():
            d.append([key, value])
        d.sort(key=lambda x: x[0])
        ans = 0
        if len(d) == 1:
            return 0

        for i in range(1, len(d)):
            # d[i][0] 升序排列
            if d[i][0] - d[i - 1][0] == 1:
                ans = max(ans, d[i - 1][1] + d[i][1])
        return ans

# @lc code=end
