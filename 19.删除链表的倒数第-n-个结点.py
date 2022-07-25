#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        forward = head
        behind = head   
        for _ in range(n):
            forward = forward.next
        # 链表长度刚好为 n 
        if not forward:
            return head.next
        # while 结束时， behind 执行倒数第 n+1 个节点
        while forward.next:
            behind = behind.next
            forward = forward.next
        # 删除倒数第 n 个（即 behind.next ）节点
        behind.next = behind.next.next
        return head

     
# @lc code=end

