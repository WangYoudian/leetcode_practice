#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# 分析与关联：这道题可以转化为寻找两个有序数组中第k小的数
#            这个思路最重要的是保证k在每个迭代中能够收敛为k - k/2
# 使得k收敛的基本的思想是，比较 A[k/2−1] 和 B[k/2−1] ，若前者大，则排除A[0...k/2-1]这 k/2 个数
# 同时k = k - k/2，反之排除B[0...k/2-1]，若二者相等，可以当做前者大处理，同样是排除k/2个数字
# 毕竟A[k/2−1] 和 B[k/2−1]前面（不包含自身）最多一共才k-2个数（若k为偶数是k-1，若k为奇数，则为k-3个数）
# 包含其中一个也就k-1个数，还没有够到第k小的最终答案

# 有以下三种情况需要特殊处理：
# 1.如果 A[k/2−1] 或者 B[k/2−1] 越界，那么我们可以选取对应数组中的最后一个元素。
# 在这种情况下，我们必须根据排除数的个数减少 k 的值，而不能直接将 k 减去 k/2。
# 2.如果一个数组为空，说明该数组中的所有元素都被排除，我们可以直接返回另一个数组中
# 第 k 小的元素。
# 3.如果 k=1，我们只要返回两个数组首元素的最小值即可。

# 注意：1.二分的目的（排除k/2个数，因此数组下标必然是k/2-1）；2.边界条件的处理

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth_element(k):
            # 记录A和B的下标位置，小于index的都已经被排除
            index1, index2 = 0, 0
            # 对常规和边界情形进行迭代，边界为退出函数的条件
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k -1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                
                # 常规不越界情形
                # 使用min，避免迭代过程中越界，同时需要注意排除时，也不再是k/2个元素
                new_index1 = min(index1 + k // 2 - 1, m - 1)
                new_index2 = min(index2 + k // 2 - 1, n - 1)
                if nums1[new_index1] <= nums2[new_index2]:
                    k = k - (new_index1 - index1 + 1)
                    index1 = new_index1 + 1
                else:
                    k = k - (new_index2 - index2 + 1)
                    index2 = new_index2 + 1

        m, n = len(nums1), len(nums2)
        total = m + n
        if total % 2 == 1:
            return get_kth_element(total // 2 + 1)
        else:
            return (get_kth_element(total // 2 + 1) + get_kth_element(total // 2)) / 2.0
# @lc code=end

''