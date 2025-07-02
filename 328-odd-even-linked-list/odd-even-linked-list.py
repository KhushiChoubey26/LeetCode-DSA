# Definition for singly-linked list (usually provided by the platform)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd = head            # pointer to odd nodes
        even = head.next      # pointer to even nodes
        even_head = even      # keep head of even nodes to connect later
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        odd.next = even_head  # attach even nodes after odd nodes
        
        return head
