# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        n = head.val
        ptr = head.next
        while ptr:
            n = (n<<1)|ptr.val
            ptr = ptr.next
        return n