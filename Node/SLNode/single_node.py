'''
    This file implements a singly linked node structure
    A singly linked node is a data structure that has a value (data) and a pointer to its next element
'''

from typing import TypeVar, Generic

T = TypeVar('T')


class SLNode(Generic[T]):
    '''
        This is the Singly Linked Node class
        This class implements the basics operations in a singly linked node structure
    '''
    def __init__(self, data: T, next=None) -> None:
        '''
            Parameters:
                data: Represents the node's value
                next: Represents the next element
            This is the class constructor. This method initialize the class' attributes
        '''
        self.data: T = data
        self.next = next
    
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
