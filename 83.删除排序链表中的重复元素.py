#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        # 防止为 head 为空
        while cur:
            # 多个连续重复的节点
            while cur.next and cur.val == cur.next.val:
                # 更新 cur.next 实质是删除 cur.next 
                cur.next = cur.next.next
            # cur 永远指向不重复的第一个节点
            cur = cur.next
        return head


# @lc code=end
