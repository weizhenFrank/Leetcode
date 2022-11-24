# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
# O(n^2) time, O(n) space
# class Solution:
#     def hasCycle(self, head) -> bool:
#         if head is None:
#             return False
#         visited_nodes = [head]
#         while True:
#             if head.next is None:
#                 return False
#             elif head.next in visited_nodes:
#                 return True
#             else:
#                 visited_nodes.append(head.next)
#             head = head.next

# O(n) time, O(1) space
class Solution:
    def hasCycle(self, head) -> bool:
        if head is None or head.next is None:
            return False
        head1 = head
        head2 = head
        while head1 is not None and head2.next is not None:
            head1 = head1.next
            head2 = head2.next.next
            if head1 == head2:
                return True
            if head2 is None:
                return False

        return False
    
