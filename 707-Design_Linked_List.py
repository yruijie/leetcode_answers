class MyLinkedList:
    class __Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = None

        def getVal(self):
            return self.val

        def getNext(self):
            return self.next

        def setVal(self, newval):
            self.val = newval

        def setNext(self, newnext):
            self.next = newnext

    def __init__(self):
        self.first = MyLinkedList.__Node(None, None)
        self.last = self.first
        self.num = 0

    def get(self, index):
        if index >= 0 and index < self.num :
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            if cursor:
                return cursor.getVal()
        else:
            return -1

    def addAtHead(self, val):
        node = MyLinkedList.__Node(val)
        node.setNext(self.first.getNext())
        if self.first.getNext() is None:
            self.last = node
        self.first.setNext(node)
        self.num += 1

    def addAtTail(self, val):
        node = MyLinkedList.__Node(val)
        self.last.setNext(node)
        self.last = node
        self.num += 1

    def addAtIndex(self, index, val):  # Still got bug
        cursor = self.first
        if index < self.num:
            for i in range(index):
                cursor = cursor.getNext()
            node = MyLinkedList.__Node(val, cursor.getNext())
            cursor.setNext(node)
            self.num += 1
        else:
            self.addAtTail(val)

    def deleteAtIndex(self, index): # Still got bug
        cursor = self.first
        if index < self.num:
            for i in range(index):
                print("In for loop-- cursor is pointing to -- " + str(cursor.getVal()))
                cursor = cursor.getNext()
            print("Now cursor is pointing to -- " + str(cursor.getVal()))
            tmp = cursor.getNext()
            cursor.setNext(tmp.getNext())
            self.num -= 1




# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
#print(obj.first.getNext() is None)
# param_1 = obj.get(index)

obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtTail(4)
obj.addAtTail(5)
obj.addAtTail(6)

obj.addAtIndex(2,9)
#obj.addAtIndex(2,8)
#obj.addAtIndex(1,4)
#obj.addAtIndex(1,3)
#obj.addAtIndex(1,4)

print(obj.get(0), obj.get(1), obj.get(2), obj.get(3), obj.get(4), obj.get(5))
#print(obj.first.getNext().getVal())

#obj.deleteAtIndex(1)
#print("After delete index 1's node: ")
#print(obj.get(0), obj.get(1), obj.get(2))

"""
以下为使用List实现的“顺序表”。虽然可以运行通过,但不符合题目的要求“链表”
class MyLinkedList:

    def __init__(self):
        self.ary = []

    def get(self, index):
        if index > len(self.ary) - 1 or index < 0:
            return -1
        return self.ary[index]

    def addAtHead(self, val):
        self.ary.insert(0, val)

    def addAtTail(self, val):
        self.ary.append(val)

    def addAtIndex(self, index, val):
        if index > len(self.ary):
            return
        elif index == len(self.ary):
            self.ary.append(val)
        else:
            self.ary.insert(index, val)

    def deleteAtIndex(self, index):
        if index > len(self.ary) - 1 or index < 0:
            return
        del self.ary[index]
"""
