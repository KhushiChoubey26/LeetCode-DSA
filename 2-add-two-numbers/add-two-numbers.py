# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()  # dummy node to hold the result list
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # value from l1 or 0
            val2 = l2.val if l2 else 0  # value from l2 or 0

            # Calculate new digit and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10

            # Append new digit to result list
            current.next = ListNode(new_digit)
            current = current.next

            # Move to next nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next
