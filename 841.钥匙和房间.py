#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        q = deque(rooms[0])
        while q:
            key = q.popleft()
            if not visited[key]:
                q.extend(rooms[key])
                visited[key] = True

        return all(visited)
# @lc code=end

