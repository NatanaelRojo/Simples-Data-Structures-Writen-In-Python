'''
    This file implements a double linked node structure
    A double linked node is a data structure that has a value (data), a pointer to its next element, and a pointer to its previous element
'''

from typing import TypeVar, Generic

T = TypeVar('T')

class DLNode(Generic[T]):
    '''
        This is the Double Linked Node class
        This class implements the basics operations in a double linked node structure
    '''
    def __init__(self, data, next = None, previous = None) -> None:
        '''
            Parameters:
                data: Represents the node's value
                next: Represents the next element
                previous: Represents the previous element
            This is the class constructor. This method initialize the class' attributes
        '''
        self.data: T = data
        self.next = next
        self.previous = previous
    
    def get_data(self) -> T:
        '''
            Return:
                data: The value in this node
            This method returns data attribute
        '''
        return self.data
    
    def get_next(self):
        '''
            Return:
                next: The next element of this node
            This method returns a reference to the next element
        '''
        return self.next
    

    def get_previous():
        '''
            Return:
                previous: The next element of this node
            This method returns a reference to the previous element
        '''
        return self.previous