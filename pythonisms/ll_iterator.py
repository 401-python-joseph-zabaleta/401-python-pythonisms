class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection): 
                self.insert(item)

    def __str__(self):
        """Overrides python String Method
        """
        output = ''

        for value in self:
            output += f'{{ {str(value)} }} --> '

        return output + 'None'

    def __iter__(self):
        """ Makes a non iteratorable object into an iterable. Allowing it to be iterated over.
        """
        
        def value_generator():

            current = self.head

            while current:
                yield current.value

                current = current.next
        
        return value_generator()

    def __len__(self):
        """ Defines the length of a data structure that normally does not have a length. Currently this is a Big O problem based on how it has to Travel O(N) times to create a list to get its length.
        """
        return len(list(iter(self)))

    def __eq__(self, other):
        """ Checks for equality between two Linked lists. Further information can be found here: https://docs.python.org/3/library/functools.html#functools.total_ordering for Data collections
        """
        return list(self) == list(other)

    def __getitem__(self, index):
        """ This allows non list objects have the ability to retrieve an item from them as if they were a list. Using an "index" value example linkedlist[0]
        """

        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item
        
        raise IndexError

    # Methods available to Linked List
    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node