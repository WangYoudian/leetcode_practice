#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        end = n - 1
        while s[end] == ' ':
            end -= 1
        start = end
        # start 必须为非负数，因为 python 中 s[-1] 是合法的
        while s[start] != ' ' and start >= 0:
            start -= 1
        return end - start
        

# @lc code=end

