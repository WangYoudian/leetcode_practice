#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
from unicodedata import digit


class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        while x != 0:
            if ans < (-2**31) // 10 + 1 or ans > (2**31 - 1) // 10:
                return 0
            digit = x % 10
            # star ※※※
            # Python3的取模运算在x小于0时，范围也是在[0,9]之间
            # 故而需要调整到[-9, 0]
            if x < 0 and digit > 0:
                digit -= 10
            # 同理，整除在x小于0时，会向下取整，因此不能写成x//10
            # 为了正负通用，故而减去digit，再做整除法
            x = (x - digit) // 10
            ans = ans * 10 + digit
        return ans

# @lc code=end

