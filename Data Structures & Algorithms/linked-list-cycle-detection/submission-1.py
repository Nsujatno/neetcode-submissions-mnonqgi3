# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        okay so logic im kinda thinking to store the nodes in a hashset
        if we see the same again then its a cycle
        if not then its not a cycle
        """
        hashset = set()
        while head:
            if head in hashset:
                return True
            hashset.add(head)
            head = head.next
        return False