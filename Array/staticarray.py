"""
    This is a basic implementation of an Array data structure. This implementation is based on Python lists.
    A static array is a sequential data structure and whose size does not change
"""

from typing import Iterator, TypeVar, Generic

T = TypeVar('T')

class StaticArray(Generic[T]):
    '''
        This is Static Array class
        This class implements the basics operations in a static array class
    '''
    def __init__(self, capacity: int, fill_value: T = None) -> None:
        '''
            Parameters:
                capacity: Represents the array's capacity that is, the number of elements it can contain
                fill_value: Represents the type of each element in the array
            This is the class constructor. This method initialize the class' attributes
        '''
        self.items: list = [fill_value for i in range(capacity)]

    def size(self) -> int:
        '''
            This function returns the size of this array
        '''
        return len(self.items)
    
    def get_item(self, index) -> T:
        '''
            Parameters:
                index: Represents the index of an element in this array
            Return:
                This function returns the element at the indicated index
        '''
        return self.items[index]
    
    def set_item(self, index: int, new_item: T) -> None:
        '''
            Parameters:
                index: Represents the index to change
                new_item: Represents the new element for indicated index
        '''
        self.items[index] = new_item
    
    def __str__(self) -> str:
        '''
            Return:
                This function returns the string representation of this structure
        '''
        return str(self.items)
    
    def __iter__(self) -> Iterator:
        '''
            Return:
                This function returns the iterator of this structure
        '''
        return iter(self.items)
    
    def __getitem__(self, index):
        '''
            Parameters:
                index: Represents the index of an element in this array
            Return:
                This function returns the element at the indicated index
        '''
        return self.items[index]
    
    def __setitem__(self, index, new_item) -> None:
        '''
            Parameters:
                index: Represents the index to change
                new_item: Represents the new element for indicated index
        '''
        self.items[index] = new_item
    
    def __len__(self) -> int:
        '''
        Return:
            This function returns the array' size
        '''
        return len(self.items)