class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None or self.tail == None

    def append(self, value: int) -> None:
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = self.head
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val
