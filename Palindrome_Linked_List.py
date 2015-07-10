#question name:Palindrome Linked List
#question link:https://leetcode.com/problems/palindrome-linked-list/
#Runtime: 188 ms

#-------------------Submitted Code-------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        l = list()
        l.append(head)
        if not head:
            return True
        if head.next == None:
            return True
        n = 1
        while l[n-1].next != None:
            l.append(l[n-1].next)
            n = n + 1
        lenth = len(l)
        for i in range(0, lenth/2):
            if l[i].val != l[lenth-1-i].val:
                return False
        return True