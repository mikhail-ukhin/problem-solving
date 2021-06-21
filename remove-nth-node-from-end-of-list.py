# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1, 2, 3, 4, 5 / n = 3

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        p1, p2 = head, head
        dummy.next = head

        for i in range(1, n + 1):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next        

        return dummy.next

    def createLinkedList(self, arr):
        head = ListNode(arr[0])
        p = head

        for v in range(1, len(arr)):
            val = ListNode(arr[v], None)
            p.next = val
            p = p.next

        return head    
