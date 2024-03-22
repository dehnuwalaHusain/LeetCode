# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_copy = l1
        l2_copy = l2
        num1 = 0
        num2 = 0
        for i in range (100):
            if (l1_copy and l2_copy):
                num1 += l1_copy.val * 10**i
                l1_copy = l1_copy.next

                num2 += l2_copy.val * 10**i
                l2_copy = l2_copy.next
            elif (l1_copy):
                num1 += l1_copy.val * 10**i
                l1_copy = l1_copy.next
            elif (l2_copy):
                num2 += l2_copy.val * 10**i
                l2_copy = l2_copy.next
            else:
                break
        res = num1 + num2
        res = [int(x) for x in str(res)]
        res = res [::-1]
        
        node = ListNode(res[0])
        curr = node
        del(res[0])
        while (res):
            tempnode = ListNode(res[0])
            curr.next = tempnode
            curr = tempnode 
            del(res[0])

        return node