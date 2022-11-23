class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iteratively
class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    
 
# recursively
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        new_head = self.helper(head)
        
        return new_head
    
    def helper(self, head, node=None):
        if head is None:
            return node

        newHead = head.next
        head.next = node
        return self.helper(newHead, head)
        
        
    
n5 = ListNode(5)
n4 = ListNode(4, next=n5)
n3 = ListNode(3, next=n4)
n2 = ListNode(2, next=n3)
n1 = ListNode(1, next=n2)

def print_node(head):
    while head:
        print(f'{head.val}')
        head = head.next
    

sol = Solution()
new_head = sol.reverseList(n1)
print_node(new_head)