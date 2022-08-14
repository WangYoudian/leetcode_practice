#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        # 1 = 2 ^ 0
        while n % 2 == 0:
            n //= 2
        return False if n != 1 else True
# @lc code=end
