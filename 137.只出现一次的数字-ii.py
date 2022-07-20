#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# 方法一：哈希表
# 使用collections.Counter计数
# 方法二：位运算

# 注意：偶数次中找奇数次，直接异或；若奇数次中找1次，total对奇数次数取余
# 剩下的就是ans的第i位（0或者1）
# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            # 将出现次数为3的数字的第i位影响消去 - 对3取余
            if total % 3:
                if i == 31:
                    # 减去2**31
                    ans -= 1 << i
                else:
                    ans += 1 << i
        return ans
                    
# @lc code=endFF

