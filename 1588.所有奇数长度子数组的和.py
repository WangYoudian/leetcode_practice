#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#
# 分析：最理想的当然是计算出每个元素在结果中贡献的次数，
#   对 xi * ci 求和
#   次一点的就是，根据奇数组的不同长度，采用滑动窗口求和
#   这种做法能够节省一定的时间，在数组长度越大时越明显

# @lc code=start

class Solution:
    # def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    #     n = len(arr)
    #     max_odd_length = n if n % 2 == 1 else n - 1
    #     ans = 0
    #     for j in range(1, max_odd_length+1, 2):
    #         # sub_sum 是首个长度为 j 的数组的和，后续使用滑动窗口维护这个和
    #         sub_sum = sum(arr[:j])
    #         # partial 是以 j 为数组长度的所有子数组的和的和
    #         partial = sub_sum
    #         for i in range(n - j):
    #             sub_sum = sub_sum + arr[i + j] - arr[i]
    #             partial += sub_sum
    #         ans += partial
    #     return ans

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # corner case
        
        res = 0; freq = 0; n = len(arr)
        for i in range(n):
            freq = freq-(i+1)//2+(n-i+1)//2
            res += freq*arr[i]
        return res

# @lc code=end
