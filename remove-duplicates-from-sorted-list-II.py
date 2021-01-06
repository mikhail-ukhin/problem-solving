# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = ListNode(-1)
        start.next = head
        p1, p2 = head, start

        while p1:
            while p1.next and p1.val == p1.next.val:
                p1 = p1.next
            if p2.next == p1:
                p2, p1 = p2.next, p1.next
            else:
                p2.next = p1.next
                p1 = p2.next
                
        return start.next