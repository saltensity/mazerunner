############################### 72 chars ###############################

from datastruct import LinkedList


class Empty(Exception):
    """
    Error raised when trying to pop/dequeue items from an empty
    Stack/Queue.
    """
        

class Stack(LinkedList):
    """
    Implements the Stack ADT using a linkedlist.

    Arguments
    ---------
    None

    Methods
    -------
    - push(item) -> None
    - pop() -> item
    """

    def __repr__(self) -> str:
        return 'Stack()'

    def push(self, item) -> None:
        """
        Pushes item onto the top of the stack.

        Arguments
        ---------
        - item
          The item to be pushed.

        Returns: None
        """
        # Replace the line below with your code
        self.append(item)

    def pop(self) -> "item":
        """
        Pops item off the top of the stack, and returns it.

        Arguments
        ---------
        None

        Returns: item

        Raises: Empty - if stack is already empty
        """
        # Replace the line below with your code
        if self.length() == 0:
            raise Empty()
        temp = self.get(self.length())
        self.delete(self.length())
        return temp


# Queue can also inherit from Array
class Queue(LinkedList):
    """
    Implements the Queue ADT using a linkedlist.

    Arguments
    ---------
    None

    Methods
    -------
    - enqueue(item) -> None
    - dequeue() -> item
    """

    def __repr__(self) -> str:
        return 'Queue()'

    def enqueue(self, item) -> None:
        """
        Enqueues item into the end of the queue.

        Arguments
        ---------
        - item
          The item to be enqueued.

        Returns: None
        """
        self.append(item)

    def dequeue(self) -> "item":
        """
        Dequeues item from the front of the queue, and returns it.

        Arguments
        ---------
        None

        Returns: item

        Raises: Empty - if queue is already empty
        """
        temp = self.get(1)
        self.delete(1)
        return temp

stack = Stack()
stack.push(100)
stack.push(10)
print(stack.pop())
print(stack.pop())
print(stack.pop())