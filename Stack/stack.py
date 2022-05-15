'''
    This file implements a stack data structure. This structure is based on simple linked list
    A stack is a Lifo (last in, first out)structure
'''

from typing import Iterable, TypeVar, Generic

from ..LList.SLList.single_linked_list import SLList

T = TypeVar('T')


class Stack(Generic[T]):
    '''
        This is the Stack class
        This class implements the basics operations of a stack
    '''
    
    def __init__(self) -> None:
        '''
            This is the class constructor. This function initialize the class' attributes
        '''
        self.items: SLList = SLList()
        self.__size: int = 0
    
    def push(self, data: T) -> None:
        '''
            This function inserts an element at the top of the stack
        '''
        self.items.appbegin(data)
        self.__size += 1
    
    def pop(self) -> T:
        '''
        Return:
                This function removes the element at the top of the stack
                and returns that element
        '''
        target  = self.items.head.data
        removed_item = self.items.delete(target)
        if removed_item == None:
            return None
        else:
            self.__size -= 1
            return removed_item
    
    def peek(self) -> T:
        '''
        Return:
                This function returns the element at the top of the stack
        '''
        return self.items.head.data
    
    def clear(self) -> None:
        '''
            This function clear the list, that is, remove the all elements
        '''
        self.items.clear()
    
    def is_empty(self) -> bool:
        '''
        Return:
                This function returns True if the stack has no elements, otherwise, returns False
        '''
        return self.items.size() == 0

    def is_in(self, data: T)-> bool:
        '''
            Parameters:
                data: Represents the element to search
            Return:
                This function returns True if the indicated element is in the stack,
                otherwise, returns False
        '''
        if self.items.search(data) == None:
            return False
        else:
            return True
        
    def search(self, data: T) -> T:
        '''
            Parameters:
                data: Represents the element to search
            Return:
                This function returns the indicated element in parameters,
                if it is in the stack , otherwise, returns None
        '''
        return self.items.search(data)
    
    def __len__(self) -> int:
        '''
        Return:
                This function returns the stacks' size
        '''
        return self.items.size()
    
    def __iter__(self):
        '''
            Return:
                This function returns the iterator of this structure
        '''
        return self.items.__iter__()
    
    def __str__(self) -> str:
        '''
        Return:
            This function returns the string representation of this structure
        '''
        return self.items.__str__()