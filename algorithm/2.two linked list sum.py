class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode("ddd")
#print(b.val)
a.next = b
#print(a.val)

def printList(node):
    while node:                #while node is not null
        print(node.val)
        node = node.next

printList(a)

# while 1:
#     print('hello')

def addTwoNumbers(l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:   #while l1 or l1 != none   carry != 0
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next

l1 = ListNode(8)
l12 = ListNode(1)
l2 = ListNode(3)
l23 = ListNode(9)
l1.next = l12
l2.next = l23
cc = addTwoNumbers(l1,l2)

printList(cc)