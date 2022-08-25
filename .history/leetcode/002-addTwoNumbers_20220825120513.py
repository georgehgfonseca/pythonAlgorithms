from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        buffer = 0
        l1Done = False
        l2Done = False
        while l1 or l2:
            l1Val = 0 if l1Done else l1.val
            l2Val = 0 if l2Done else l2.val
            if l1Val + l2Val + buffer > 9:
                ans = ans + [l1Val + l2Val + buffer - 10]
                buffer = 1
            else:
                ans = ans + [l1Val + l2Val + buffer]
                buffer = 0
            if not l1Done:
                l1 = l1.next
                if not l1:
                    l1Done = True
            if not l2Done:
                l2 = l2.next
                if not l2:
                    l2Done = True
        if buffer == 1:
            ans = ans + [1]
        # converting ans into ListNodes
        ansListNodePrev = ListNode(ans[-1])
        if len(ans) > 1:
            for i in range(len(ans) - 2, -1, -1):
                ansListNode = ListNode(ans[i], ansListNodePrev)
                ansListNodePrev = ansListNode
            return ansListNode
        else:
            return ansListNodePrev

    def addTwoNumbersArray(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        buffer = 0
        l1Done = False
        l2Done = False
        while l1 or l2:
            l1Val = 0 if l1Done else l1.val
            l2Val = 0 if l2Done else l2.val
            if l1Val + l2Val + buffer > 9:
                ans = ans + [l1Val + l2Val + buffer - 10]
                buffer = 1
            else:
                ans = ans + [l1Val + l2Val + buffer]
                buffer = 0
            if not l1Done:
                l1 = l1.next
                if not l1:
                    l1Done = True
            if not l2Done:
                l2 = l2.next
                if not l2:
                    l2Done = True
        if buffer == 1:
            ans = ans + [1]
        return ans


testCases = [
    (ListNode(0), ListNode(0)),
    (
        ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
    ),
]
s = Solution()
for t in testCases:
    print(s.addTwoNumbers(t[0], t[1]))
