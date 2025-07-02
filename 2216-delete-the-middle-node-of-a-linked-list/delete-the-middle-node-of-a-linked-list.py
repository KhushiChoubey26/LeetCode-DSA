class Solution:
    def deleteMiddle(self, head):
        # If only one node, return None
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        # Move fast pointer by 2 and slow pointer by 1
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        prev.next = slow.next
        
        return head
