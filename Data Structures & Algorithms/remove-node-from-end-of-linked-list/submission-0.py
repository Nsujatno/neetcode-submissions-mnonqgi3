# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodes = []
        count = 1
        while curr:
            nodes.append(curr)
            curr = curr.next
        for i in range(len(nodes)-1, -1, -1):
            if count == n:
                nodes.pop(i)
                print("popped")
                break;
            print(nodes[i].val)
            count += 1
        for i in range(len(nodes)):
            if i == len(nodes)-1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]
        if len(nodes) == 0:
            return None
        return nodes[0]