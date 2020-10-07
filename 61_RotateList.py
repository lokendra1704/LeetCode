# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        ptr = head
        size = 0
        while ptr:
            size+=1
            ptr = ptr.next
        ptr = head
        k%=size
        t = k
        bucket = []
        while ptr:
            bucket.append(ptr.val)
            if t>0:
                t-=1
            elif t==0:
                ptr.val = bucket.pop(0)
            ptr = ptr.next
        ptr = head
        while k>0:
            ptr.val = bucket.pop(0)
            ptr = ptr.next
            k-=1
        return head
        