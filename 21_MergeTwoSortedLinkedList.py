# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        cur = head = ListNode()
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = ListNode(p1.val)
                p1 = p1.next
            else:
                cur.next = ListNode(p2.val)
                p2 = p2.next
            cur = cur.next
        p3 = p1 if p1 else p2
        while p3:
            cur.next = ListNode(p3.val)
            p3 = p3.next
            cur = cur.next
        return head.next