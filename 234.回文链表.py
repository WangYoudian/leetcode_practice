#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        arr = [head.val]
        cur = head.next
        while cur:
            arr.append(cur.val)
            cur = cur.next
        for i in range(len(arr)//2):
            if arr[i] != arr[len(arr) - i - 1]:
                return False
        return True
# @lc code=end

