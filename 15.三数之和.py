#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
# 首先对数组进行排序，解决三元组的重复问题（假定a<=b<=c）
# 搜索策略为：定1动2，当a确定时，b从小到大搜索，c从大到小搜索
# 且b和c为并列关系，跳出三重循环的大框架，继续优化

# 「双指针」，当我们需要枚举数组中的两个元素时，
# 如果我们发现随着第一个元素的递增，第二个元素是递减的，
# 那么就可以使用双指针的方法

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for first in range(n-2):
            # 三个正数的和不可能是0
            if nums[first] > 0:
                break
            # a出现连续重复数字
            if first > 0 and nums[first] == nums[first -1]:
                continue

            target = -nums[first]
            third = n -1
            for second in range(first+1, n-1):
                # b出现连续重复数字，下标后移以避免得到重复的三元组
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                # third由最大下标变小，若开始时b+c<0，
                # 则直接退出while，检查b和c之和是否等于target
                # star ※※ - 这里a、b为定，只动c，因此循环只在>target情况下继续
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # b和c指针重合，下一次b后移则，不满足b<=c，直接退出b的这层循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


# @lc code=end

