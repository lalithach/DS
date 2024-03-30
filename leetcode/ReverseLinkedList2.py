# Definition for singly-linked list.
# Leetcode 92
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevNode = dummy
        currNode = head
        for i in range(0, left-1):
            prevNode = prevNode.next
            currNode = currNode.next
        
        subHead = currNode
        
        preNode = None
        for i in range(0, right-left+1):
            nextNode = currNode.next
            currNode.next = preNode
            preNode = currNode
            currNode = nextNode

        prevNode.next = preNode
        subHead.next = currNode
        return dummy.next



    
