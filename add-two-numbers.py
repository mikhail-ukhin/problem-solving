# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode(-1)
        pointer = start
        tr = False
        
        while l1 or l2 or tr:
           c_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + (1 if tr else 0)
           tr = c_sum >= 10

           pointer.next = ListNode(c_sum % 10)

           l1 = l1.next if l1 else None
           l2 = l2.next if l2 else None
           pointer = pointer.next

        return start.next

    def createListFromArray(self, arr):
        start = ListNode(arr[0])
        pointer = start

        for v in arr[1:]:
            pointer.next = ListNode(v)
            pointer = pointer.next

        return start

    def printLinkedList(self, node:ListNode):
        while node:
            print(node.val)
            node = node.next  
