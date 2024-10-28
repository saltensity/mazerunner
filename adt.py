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

    def __repr__(self):
        return 'Stack()'

    def push(self, item):
        """
        Pushes item onto the top of the stack.

        Arguments
        ---------
        - item
          The item to be pushed.

        Returns: None
        """
        # Replace the line below with your code
        raise NotImplementedError

    def pop(self):
        """
        Pops item off the top of the stack, and returns it.

        Arguments
        ---------
        None

        Returns: item

        Raises: Empty - if stack is already empty
        """
        # Replace the line below with your code
        raise NotImplementedError


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

    def __repr__(self):
        return 'Queue()'

    def enqueue(self, item):
        """
        Enqueues item into the end of the queue.

        Arguments
        ---------
        - item
          The item to be enqueued.

        Returns: None
        """
        # Replace the line below with your code
        raise NotImplementedError

    def dequeue(self):
        """
        Dequeues item from the front of the queue, and returns it.

        Arguments
        ---------
        None

        Returns: item

        Raises: Empty - if queue is already empty
        """
        # Replace the line below with your code
        raise NotImplementedError
