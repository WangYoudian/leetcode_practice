#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
# 分析：小镇法官一定是拥有最多人信任的人，因此，流程上
#       先找出被信任最多的人，然后确认此人是否有信任别人
from collections import defaultdict


# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(int)
        trusting = set()
        candidate, cnt = 1, 0
        # 2, []（输出-1）和1, []（输出1）
        if not trust:
            return 1 if n == 1 else -1
        for a, b in trust:
            trusting.add(a)
            trusted[b] += 1
            if trusted[b] > cnt:
                cnt = trusted[b]
                candidate = b
        # 法官不能信任他人，且获取信任数为n - 1
        if candidate in trusting or cnt < n - 1:
            return -1
        return candidate

# @lc code=end

