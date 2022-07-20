#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#
# 方法一：逐位操作
# 方法二：分治运算（16+16->8+8）

# *总结：整型的位运算，一般确定是32位的位运算
# 在 Python 的实现中，因为 Python 的整数类型为是无限长的，
# 所以无论怎样左移位都不会溢出。因此，我们需要对 Python 中
# 的整数进行额外处理，以模拟用补码表示的 32 位有符号整数类型。
# 具体地，我们将整数对 2^32 取模，从而使第 33 位及更高位均为 00；
# 因为此时最终结果为用补码表示的包含符号位的 32 位整数，
# 所以我们还需要再次将其换算为 Python 的整数。


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        i = 0
        while i < 32 and n > 0:
            # n的最低位（n & 1）放到ans的最高位
            ans |= (n & 1) << (31 - i)
            i += 1
            n >>= 1
        return ans
        
# @lc code=end

