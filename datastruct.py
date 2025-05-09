############################### 72 chars ###############################

class Node:
    """
    Represents a node in a linkedlist.

    Arguments
    ---------
    - data
      The data encapsulated in the node.

    Attributes
    ----------
    - next: Node | None
      The next node in the linkedlist, or None if the node is the tail.

    Methods
    -------
    - get() -> data
      Return the data stored in the node.
    """

    def __init__(self, data):
        # Replace the line below with your code
        self._data = data
        self.next = None
        

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self):
        """Return the data stored in the node.

        Arguments
        ---------
        None

        Return: data
        """
        return self._data


class LinkedList:
    """
    Represents a sequence of data items.

    Arguments
    ---------
    None

    Attributes
    ----------
    None

    Methods
    -------
    - length() -> int
    - get(index) -> item
    - insert(index, item) -> None
    - append(item) -> None
    - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
        ---------
        None

        Return: int
        """
        length = 0
        currentNode = self._head
        while currentNode is not None:
          length += 1
          currentNode = currentNode.next
        
        return length
        

    def get(self, n: int) -> "item":
        """Returns item at n-th node.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: item

        Raises: IndexError if n > length
        """
        if n > self.length():
          raise IndexError
  
        currentNode = self._head
        for i in range(n-1):
          currentNode = currentNode.next
        
        return currentNode.get()

    def insert(self, n: int, item) -> None:
        """Insert item into linkedlist at position n.
        insert at head -> n == 0
        append -> n == length

        Arguments
        ---------
        - n: int
          sequence number of item to be inserted.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        
        currentNode = self._head
        
        node = Node(item)
        if n == 1:
          self._head = node
          self._head.next = currentNode
          return
        
        for i in range(n-1):
          currentNode = currentNode.next
          print(currentNode)
          
        if n == self.length():
          currentNode.next = node
        else:
          next = currentNode.next
          node.next = next
          currentNode.next = node
        
        #raise NotImplementedError

    def append(self, item) -> None:
        """Append item at the end of linkedlist.

        Arguments
        ---------
        - item
          The item to be appended.

        Returns: None
        """
        if self.length() == 0:
          self._head = Node(item)
          return
        
        node = Node(item)
        currentNode = self._head
        
        while currentNode.next != None:
          currentNode = currentNode.next
          
        currentNode.next = node
        
        # raise NotImplementedError

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: None

        Raises: IndexError if n > length
        """
        currentNode = self._head
        for i in range(n-2):
           currentNode = currentNode.next
        
        if n == 1:
          self._head = self._head.next
        elif n == self.length():
          currentNode.next = None
        else:
          prev = currentNode
          next = currentNode.next.next
          prev.next = next
      

    def contains(self, item) -> bool:
        """Checks whether an item is in the linkedlist and returns
        a boolean value to indicate the status of the search

        Arguments
        ---------
        - item
          The item to be searched for.

        Returns: True if item is found in the linkedlist,
        otherwise False
        """
        currentNode = self._head
        while currentNode is not None:
          if currentNode.get() == item:
              return True
          
          currentNode = currentNode.next
        
        return False

# linkedlist = LinkedList()
# linkedlist.append(69)
# linkedlist.append(100)
# linkedlist.insert(1, 9)
# print(linkedlist.get(1))
# print(linkedlist.get(2))
# print(linkedlist.get(3))
# print(linkedlist.contains(67))
# linkedlist.delete(1)

# 9 69 100