#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) == 0:
            return 0
        
        # 先利用 sign 和 offset 处理符号问题（影响：1.返回值；2.扫描位置）
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            offset = 1
        else:
            offset = 0
        ans = 0
        p = offset
        # 当下一个读入字不是数字时，停止读
        while p < len(ls) and ls[p].isdigit():
            ans = ans * 10 + ord(ls[p]) - ord('0')
            p += 1
        # 模拟截断（上溢和下溢）
        return max(-2**31, min(sign * ans, 2**31 - 1))
        
# @lc code=end

