#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def teardown(head):
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            res = 0
            n = len(arr)
            for i in range(n):
                res += arr[n - i - 1]
                if i < n - 1:
                    res *= 10
            return res
        
        def build(num):
            res = ListNode()
            head = ListNode(num % 10)
            num %= 10
            res.next = head
            while num > 0:
                num %= 10
                head.next = ListNode(num % 10)
                head = head.next
            return res
        
        a = teardown(l1)
        b = teardown(l2)
        return build(a + b)

# @lc code=end

