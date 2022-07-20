#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
# 『双指针』

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            # 左右边界最大不一定容量最大，使用ans记录历史最大值
            ans = max(ans, area)
            # 每次总是移动左右指针中，高度较低的那个
            # 想象逐渐注水，总是短板先漏水，需要找到更高的那个
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


# @lc code=end

