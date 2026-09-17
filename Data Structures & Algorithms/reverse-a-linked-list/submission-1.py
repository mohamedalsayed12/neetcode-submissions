# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #setting previous to non because linked lists start with none 
        #and setting curr to head because thats where the linked lists start
        prev, curr = None, head
        #while current is not none the loop continues to the next number 
        while curr != None:
            #next becomes the current number 
            next = curr.next
            #this is where the reversal occurs 
            curr.next = prev
            #previous number is now current 
            prev = curr
            #next previous number 
            curr = next
        return prev

            

        
     


    