class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class ListHeader:
    def __init__(self):
        self.head = None

    def addFirst(self, value):
        newnode = ListNode(value)
        newnode.next = self.head
        self.head = newnode

    def addLast(self, value):
        newnode = ListNode(value)
        if self.head is None:
            self.head = newnode
            return
        start = self.head
        while start.next is not None:
            start = start.next
        start.next = ListNode(value)

    def find(self, value):
        start = self.head
        while start is not None:
            if start.value == value:
                return "found"
            start = start.next
            return "Not found"

    def traverse(self):
        start = self.head
        while start is not None:
            print(start.value, end=",")
            start = start.next

    def count(self):
        n = 0
        start = self.head
        while start is not None:
            start = start.next
            n = n + 1
        print(n)

    def delete(self, value):
        if self.head == None:
            return
        if self == value:
            p = self.head
            self.head = p.next
            del (p)
            return
        p = self.head
        if p.next == None:
            return
        q = p.next
        while q.next is not None:
            if q.value == value:
                p.next = q.next
                del (q)
                return
            p = q
            q = q.next
        if q.value == value:
            p.next = q.next
            del (q)
            return

    def reverse(self):
        p = self.head
        if p == None:
            return

        if p.next == None:
            return
        p = self.head
        q = p.next
        if q.next == None:
            p.next = None
            q.next = p
            self.head = q
            return
        r = q.next
        while (r.next != None):
            q.next = p
            p = q
            q = r
            r = r.next
        q.next = p
        r.next = q
        self.head.next = None
        self.head = r

    def addSorted(self, value):
        newnode = ListNode(value)
        if self.head == None:
            self.head = newnode
            newnode.next = None
            return

        if value <= self.head.value:
            newnode.next = self.head
            self.head = newnode
            return
        p = self.head
        if p.next == None:
            p.next = newnode
            newnode.next = None
            return
        q = p.next
        while value > q.value and q.next is not None:
            p = q
            q = q.next
        if value <= q.value:
            p.next = newnode
            newnode.next = q
            return
        q.next = newnode
        newnode.next = None


if __name__ == '__main__':
    head = ListHeader()
    for i in range(1, 6):
        head.addLast(i)
    # head.addLast(1)
    # head.addLast(2)
    # head.addLast(3)
    # head.delete(2)
    # head.reverse()
    head.addSorted(3)
    head.traverse()
    # head.count()
