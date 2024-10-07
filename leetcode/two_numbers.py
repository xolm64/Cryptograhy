#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.


class Solution(object):
   def addTwoNumbers(self, l1, l2):
    self.l1 = l1
    self.l2 = l2
    new_l1 = []
    new_l2 = []
    i  = 0
    i2 = 0
    for elem in l1:
        new_l1.insert(i, elem)
        i = i - 1
    for elem in l2:
        new_l2.insert(i2, elem)
        i2 = i2 - 1

    int1 = str()
    for elem in new_l1:
        elem = str(elem)
        int1 = int1 + elem

    int2 = str()
    for elem in new_l2:
        elem = str(elem)
        int2 = int2 + elem

    int_result = int(int1) + int(int2)

    list_result = []
    for elem in str(int_result):
        elem = int(elem)
        list_result.append(elem)

    i = 0
    new_list_result = []
    for elem in list_result:
        new_list_result.insert(i, elem)
        i = i - 1

    return new_list_result


l1 = [2,4,3]
l2 = [5,6,4]

print(Solution().addTwoNumbers([2,4,3],[5,6,4]))