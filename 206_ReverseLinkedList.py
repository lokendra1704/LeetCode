class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur, future = None, head, None
        while cur:
            future = cur.next
            cur.next = prev
            prev = cur
            cur = future
        return prev

    #Recursive
    def recur(self, head):
        if not head: return head
        if not head.next : return head
        node = recur(head.next)
        head.next.next = head
        head.next = None
        return node
