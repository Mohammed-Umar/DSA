# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        elements_a = []
        elements_b = []

        current = l1
        while current:
            elements_a.append(str(current.val))
            current = current.next
        
        current = l2
        while current:
            elements_b.append(str(current.val))
            current = current.next

        elements_a.reverse()
        elements_b.reverse()

        num_a = "".join(elements_a)
        num_b = "".join(elements_b)

        res_add = int(num_a) + int(num_b)

        res_str = str(res_add)[::-1]
        
        dummy = ListNode(0)
        curr = dummy
        for ch in res_str:
            curr.next = ListNode(int(ch))
            curr = curr.next
        return dummy.next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)  # Dummy head to simplify building the result list
#         current = dummy
#         carry = 0
        
#         # Loop while there are nodes left in l1 or l2, or a remaining carry
#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
            
#             # Calculate sum and new carry
#             total = val1 + val2 + carry
#             carry = total // 10
            
#             # Append new digit node to result list
#             current.next = ListNode(total % 10)
#             current = current.next
            
#             # Advance input list pointers if available
#             if l1: l1 = l1.next
#             if l2: l2 = l2.next
            
#         return dummy.next
        