# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            print(head)
            return None
        reverse_ = ListNode(head.val, None)
        def reverse(link, rev):
            if link.next:
                rev = ListNode(link.next.val, rev)
                rev = reverse(link.next, rev)
            return rev
            
        
        result = reverse(head, reverse_)
        return result