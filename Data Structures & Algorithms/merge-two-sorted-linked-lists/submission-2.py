# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        One pass
        At each node, compare the two nodes
        Whichever is smaller, append that to the sorted list
        iterate both that list and the sorted list pointers
        repeat until one list is exhausted

        after this, there may be nodes still left over in the other list
        so check if any of the lists have nodes left. if they do, append all
        of them to the end of the sorted list
        """
        head = node = ListNode()
        while list1 and list2:
            # compare the two nodes
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
                node = node.next
            else:
                node.next = list2
                list2 = list2.next
                node = node.next
        # check if there are any lists remaining and append
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        return head.next
