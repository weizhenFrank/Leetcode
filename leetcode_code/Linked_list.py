# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head):
#         prev, curr = None, head
#         while curr is not None:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp

#         return prev
    
# recursion
# class Solution:
#     def reverseList(self, head):
        
#         if head is None or head.next is None:
#             return head
        

#         return 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        new_head = self.helper(head)
        
        return new_head
    
    def helper(self, next, head=None):
        if next is None or next.next is None:
            return head


        temp = head.next.next
        head.next.next = head
        head.next.next = head
        head.next = prev
        prev = next
        head = temp
        # 
        return self.helper(next, prev)
        
        
    
n5 = ListNode(5)
n4 = ListNode(4, next=n5)
n3 = ListNode(3, next=n4)
n2 = ListNode(2, next=n3)
n1 = ListNode(1, next=n2)

def print_node(head):
    while head:
        print(f'{head.val}')
        head = head.next
    
# print_node(n1)
sol = Solution()
new_head = sol.reverseList(n1)
print_node(new_head)