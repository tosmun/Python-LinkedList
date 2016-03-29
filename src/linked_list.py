"""
A basic doubly linked list implementation
@author taylor.osmun
"""
class LinkedList(object):
    """
    Internal object representing a node in the linked list
    @author taylor.osmun
    """
    class _Node(object):
        def __init__(self, _data=None, _next=None, _prev=None):
            self.data = _data
            self.next = _next
            self.prev = _prev
    """
    Construct a new linked list
    """
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0
    """
    @return True IFF the list is empty
    """
    def empty(self):
        return len(self) <= 0
    """
    Adds the given data to the beginning of the list
    @param data: The data to add
    """
    def add_first(self, data):
        node = LinkedList._Node(data, _next=self._first)
        if self._first is None:
            self._first = node
            self._last = node
        else:
            self._first.prev = node
            self._first = node
        self._size += 1
    """
    Adds the given data to the end of the list
    @param data: The data to add
    """
    def add_last(self, data):
        node = LinkedList._Node(data, _prev=self._last)
        if self._first is None:
            self._first = node
            self._last = node
        else:
            self._last.next = node
            self._last = node
        self._size += 1
    """
    Removes and returns the first element in the list
    @return The first element in the list
    @raise EmptyListException: If the list is empty when removal is attempted
    """
    def remove_first(self):
        if self.empty():
            raise EmptyListException()
        ret = self._first
        self._first = ret.next
        if self._first is not None:
            self._first.prev = None
        else:
            self._last = None
        self._size -= 1
        return ret.data
    """
    Removes and returns the last element in the list
    @return The last element in the list
    @raise EmptyListException: If the list is empty when removal is attempted
    """
    def remove_last(self):
        if self.empty():
            raise EmptyListException()
        ret = self._last
        self._last = ret.prev
        if self._last is not None:
            self._last.next = None
        else:
            self._first = None
        self._size -= 1
        return ret.data
    def __len__(self):
        return self._size
    def __iter__(self):
        node = self._first
        while node is not None:
            yield node.data
            node = node.next
    def __str__(self):
        return '[%s]'%(','.join(map(str, self)))
"""
Thrown when a removal is attempted and the list is empty
@author taylor.osmun
"""
class EmptyListException(IndexError):
    def __init__(self):
        super(EmptyListException, self).__init__()
