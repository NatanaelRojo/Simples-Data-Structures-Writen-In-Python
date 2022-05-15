'''
    This file implements a queue data structure. This structure is based on singly linked list
    A queue is a FIFo  (first in, first out)structure
'''

from typing import Iterable, TypeVar, Generic

from ..LList.SLList.single_linked_list import SLList

T = TypeVar('T')

class Queue(Generic[T]):
    '''
        This is the Queue class
        This class implements the basics operations of a queue
    '''

    def __init__(self) -> None:
        '''
            This is the class constructor.
            This function initialize the class' attributes
        '''
        self.items = SLList()
        self.__size = self.items.size()
    
    def put(self, data: T) -> None:
        '''
        This function puts an element in the queue
        '''
        self.items.append(data)
        self.__size += 1
    
    def pop(self) -> T:
        '''
            Return:
                This function removes the first element of the queue
                and returns that element
        '''
        data = self.items.head.data
        removed_item = self.items.delete(data)
        if removed_item == None:
            return removed_item
        else:
            self.__size -= 1
            return removed_item
    
    def is_empty(self) -> bool:
        '''
        Return:
                This function returns True if the queue has no elements,
                otherwise, returns False
        '''
        return self.__size == 0

    def is_in(self, data) -> bool:
        '''
            Parameters:
                data: Represents the element to search
            Return:
                This function returns True if the indicated element is in the queue,
                otherwise, returns False
        '''
        if self.items.search(data) == None:
            return False
        else:
            return True
        
    def search(self, data):
        '''
            Parameters:
                data: Represents the element to search
            Return:
                This function returns the indicated element in parameters,
                if it is in the queue , otherwise, returns None
        '''
        return self.items.search(data)
    
    def __iter__(self):
        '''
            Return:
                This function returns the iterator of this structure
        '''
        return self.items.__iter__()
    
    def __len__(self) -> int:
        '''
        Return:
                This function returns the stacks' size
        '''
        return self.items.size()
    
    def __str__(self) -> str:
        '''
        Return:
            This function returns the string representation of this structure
        '''
        return self.items.__str__()