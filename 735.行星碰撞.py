#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#

# @lc code=start
import ast
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        if n < 2:
            return asteroids
        ans = []

        def modify(arr, negative):
            if len(arr) == 0:
                arr.append(negative)
                # 递归结束条件,由于修改都是in-place,这里可以直接返回void
                return
            if arr[-1] > 0:
                if arr[-1] + negative < 0:
                    arr.pop()
                    modify(arr, negative)
                elif arr[-1] + negative == 0:
                    arr.pop()
                else:
                    pass
            else:
                ans.append(negative)

        for mass in asteroids:
            if mass > 0:
                ans.append(mass)
            elif mass < 0:
                modify(ans, mass)
        return ans

# @lc code=end
