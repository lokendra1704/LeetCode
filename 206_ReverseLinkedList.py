class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur, future = None, head, None
        while cur:
            future = cur.next
            cur.next = prev
            prev = cur
            cur = future
        return prev