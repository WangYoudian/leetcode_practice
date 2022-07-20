#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# 思路：解集数量为2**n，其中n为数组nums的长度

from typing import List

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**len(nums)):
            bits = reversed(str(bin(i)))
            result = []
            for j, s in enumerate(bits):
                if s == '1':
                    result.append(nums[j])
            ans.append(result)
        return ans


# @lc code=end

