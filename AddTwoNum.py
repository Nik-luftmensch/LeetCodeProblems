class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
def printLl(list):
    if list is None:
        return ""
    return str(list.data)+"-->"+printLl(list.next)

class Solution:
    def AddTwoNum(self,l1,l2):
        p1 = l1
        p2 = l2 
        carry = 0
        head = cur = Node(0)

        while p1 or p2 or carry:

            print(p1.data,p2.data,carry)
            
            current = carry
            current += 0 if p1 is None else p1.data
            current += 0 if p2 is None else p2.data
            if current >= 10:
                current -= 10
                carry = 1
            else:
                carry = 0
            
            cur.next = Node(current)
            cur = cur.next

            # Add base cases for iterating linked lists.
            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next

        print('exiting...')
        print('')
        return head.next
    

l1 = Node(7)
l1.next = Node(4)
l1.next.next = Node(5)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(3)

l = Solution()
l3 = l.AddTwoNum(l1,l2)

print(printLl(l1))
print(printLl(l2))
print(printLl(l3))
