# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = head
        while (ans and ans.next):
            if ans.val == ans.next.val:
                ans.next = ans.next.next
            else:
                ans = ans.next
        return head


        