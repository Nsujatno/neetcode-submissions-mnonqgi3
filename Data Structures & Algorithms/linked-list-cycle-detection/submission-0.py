# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        index = 0
        while(head):
            if head in hashset:
                return True
            hashset.add(head)
            index = index + 1
            head = head.next
        index = -1
        return False
