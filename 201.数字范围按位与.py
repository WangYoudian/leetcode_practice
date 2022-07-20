#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#
# 方法一：
# 这个问题等价于：给定两个整数，我们要找到它们对应的二进制字符串的公共前缀
# 通过二进制证明——一定存在x和x+1使得，任何小于或等于x的数，第i+1位是0
# 任何大于等于x+1的第i+1位是1，且x的i+1位后均为1，x+1的i+1位后均为0
# 这样，m到n区间的数字与运算的结果是m到n之间数字的前缀，也即是m和n的前缀

# 方法二：
# Brian Kenighan算法 —— 清除二进制串中最右边的1
# 运算：x & (x-1)
# 

# @lc code=start
class Solution:
    # def rangeBitwiseAnd(self, left: int, right: int) -> int:
    #     # 移位操作
    #     i = 0
    #     while left != right:
    #         left = left >> 1
    #         right = right >> 1
    #         i += 1
    #     ans = left << i
    #     return ans

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        n = right
        while n > left:
            n = n & (n - 1)
        return n
            
        
# @lc code=end

