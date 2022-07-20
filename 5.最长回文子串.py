#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# 回文串是天生具有状态转移性质的

# @lc code=start
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if n < 2:
    #         return s
    #     # *记录最大回文串长度与起始位置，返回值需要这两个变量*
    #     max_len = 1
    #     begin = 0
    #     # dp[i][j] 表示 s[i..j] 是否是回文串
    #     dp = [[False] * n for _ in range(n)]
    #     for i in range(n):
    #         dp[i][i] = True
        
    #     # 递推开始
    #     # 先枚举子串长度
    #     for L in range(2, n + 1):
    #         # 枚举左边界，左边界的上限设置可以宽松一些
    #         for i in range(n):
    #             # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
    #             j = L + i - 1
    #             # 如果右边界越界，就可以退出当前循环
    #             if j >= n:
    #                 break
                    
    #             if s[i] != s[j]:
    #                 dp[i][j] = False 
    #             else:
    #                 if j - i < 3:
    #                     dp[i][j] = True
    #                 else:
    #                     dp[i][j] = dp[i + 1][j - 1]
                
    #             # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
    #             if dp[i][j] and j - i + 1 > max_len:
    #                 max_len = j - i + 1
    #                 begin = i
    #     return s[begin:begin + max_len]


    # 中心扩展法
    def expand_around_center(self, string, left, right):
        """
        假定输入的string[left...right]是回文，寻找向两边扩展的极限
        """
        # 由于需要执行left-1, right+1，left下标需要大于0，right下标需要小于n-1
        # 但在返回时做一次left+1，right-1，就可以将left=0，right=n-1这两类边界包含进去
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        # 记录回文串左右边界
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expand_around_center(s, i, i)
            left2, right2 = self.expand_around_center(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]


# @lc code=end

