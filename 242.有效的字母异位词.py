#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = Counter(s)
        td = Counter(t)
        # 防止s和t中一个为真子集
        if len(sd.keys()) != len(td.keys()):
            return False
        for key in sd.keys():
            if sd[key] != td[key]:
                return False
        return True
# @lc code=end

