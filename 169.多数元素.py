#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# 方法一：
# 常规思路：对数组中每个元素进行计数，找出大于 ⌊ n/2 ⌋ 次数的元素
# 复杂度：时间复杂度为O(n^2)
# 方法二：分治算法，数组nums中的众数，一定是nums[0...n/2]的众数
# 分为左右两个子问题解决，然后选取count更大的候选值
# 方法三：Boyer-Moore投票算法
# 投票算法证明：

# 如果候选人不是maj 则 maj,会和其他非候选人一起反对 
#   会反对候选人,所以候选人一定会下台(maj==0时发生换届选举)
# 如果候选人是maj , 则maj 会支持自己，
#   其他候选人会反对，同样因为maj 票数超过一半，所以maj 一定会成功当选

# @lc code=start
class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     def major_element_count(lo, hi):
    #         if lo == hi:
    #             return nums[lo]

    #         mid = (hi + lo) // 2
    #         left = major_element_count(lo, mid)
    #         right = major_element_count(mid + 1, hi)
            
    #         # 若左半数组和右半数组众数相同，直接返回，不需要对比出现次数
    #         if left == right:
    #             return left
            
    #         left_count = sum(1 for num in nums[lo:hi+1] if num == left)
    #         right_count = sum(1 for num in nums[lo:hi+1] if num == right)
            
    #         return left if left_count > right_count else right
    #     return major_element_count(0, len(nums)-1)         

    # 投票算法
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
              
        
# @lc code=end

