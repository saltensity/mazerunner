############################### 72 chars ###############################
TAIL = 'tail'
HEAD = 'head'

class CircularQueue:
    """
    Circular Queue implemented as Array.

    Methods
    -------
    - enqueue(item)
      Adds item at the end of the queue.
    
    - dequeue()
      Returns the first item in the queue.
    """
      

    def __init__(self, size: int):
        # Delete the line below and write your code here
        self.data = [None] * size
        self.head = -1
        self.tail = 0
        self.size = size

    def _increment(self, toIncrement):
      if toIncrement == TAIL:
        self.tail += 1
        self.tail %= self.size
      else:
        self.head += 1
        self.head %= self.size
    
    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"
    
    def isempty(self):
       return self.head == -1
    
    def isfull(self):
       if self.tail == -1:
          return False
       return (self.tail+1) % self.size == self.head

    def enqueue(self, data) -> None:
        """
        Add item at the end of the queue.

        Arguments
        ---------
        - item
          The item to be added.

        Return: None
        """
        if self.isfull():
          raise Exception("Queue is full!")
        
        if self.head == -1:
           self.head = self.tail
        
        self.data[self.tail] = data
        self._increment(TAIL)
        
        if self.tail == self.head:
          self.head = -1
        
      
    def dequeue(self) -> "item":
        """
        Return the item at the head of the queue.

        Arguments
        ---------
        None

        Return: item
        """
        if self.isempty():
          raise Exception("Queue is empty!")

        #print(self.data, self.head, self.tail)
        
        # Delete the line below and write your code here
        temp = self.data[self.head]
        self.data[self.head] = None
        self._increment(HEAD)
        
        return temp
        
        # raise NotImplementedError("dequeue not implemented")
        
    def display(self):
      """
      Displays the contents of the queue from the head index to the tail index
      """
      pointer = self.head
      while pointer != self.tail:
        print(self.data[pointer], end=" ")
        pointer = (pointer + 1) % self.size
      
      print('')
      return

if __name__ == "__main__":
  cq = CircularQueue(5)
  cq.enqueue(5)
  cq.enqueue(6)
  cq.enqueue(7)
  
  cq.display()
  cq.dequeue()
  cq.display()

  cq.enqueue(5)
  cq.enqueue(6)
  
  cq.display()