"""
Inplace Solution
Rather than creating a new Node everytime, This solution modifies first linked list.
(Incase l1 is shorter than l2, then: after l1 ends, A new Listnode is appended at end untill requirement)
"""
class ListNode:             #Ignore This Line
    pass
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        cur = p1
        carry = 0
        while p1 or p2:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            sm = x + y + carry
            carry = sm//10
            val = sm%10
            if p1 and not p1.next:
                cur = p1
            if p1:
                p1.val = val
                p1 = p1.next
            else:
                cur.next = ListNode(val)
                cur = cur.next
            if p2: p2 = p2.next
        if carry: cur.next = ListNode(carry)
        return l1