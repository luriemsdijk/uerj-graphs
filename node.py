class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'


class LinkedList:
    def __init__(self, name):
        self.name = name
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next != None:
                current = current.next
                out += str(current.value) + ''
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def remove(self, value):
      if self.first != None:
        current = self.first
        if(current.value == value):
          self.first = current.next
          return current.value
        while current.value != value and current.next != None:
          previous = current
          current = current.next
        if(current.value == value):
          previous.next = current.next
          return current.value
      return False

    def getList(self):
      return self.listMe(self.first, [])

    def listMe(self, node, l):
      if(node == None):
        return l
      else:
        l.append(node.value)
        return self.listMe(node.next, l)

    def contains(self, value):
      current = self.first
      while True:
        if(current == None):
          return False
        if(current.value == value):
          return True
        if(current.next == None):
          return False
        current = current.next


# L = LinkedList()
# L.insert(1)
# L.insert(2)
# print("Listing",L.getList())
# L.insert(3)
# L.insert(4)
# print("removed: ",L.remove(4))
# print(L)
# L.clear()
# print(L)

