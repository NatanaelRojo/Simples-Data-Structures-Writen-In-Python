"""
    This files contains te implementation of a bidimentional array.
    This class is based on Python lists.
"""

from typing import TypeVar, Generic

from .staticarray import Array

T = TypeVar('T')

class Grid(Generic[T]):
    '''
        This is the Grid class
        This class implements the basics operations in a grid class
    '''
    def __init__(self, rows: int, columns: int, value_type: T = None) -> None:
        '''
            Parameters:
                rows: Represents the number of elements in each column
                column: Represents the number of columns in the grid
            This is the class constructor. This method initialize the class' attributes
        '''
        self.value_type = value_type
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, value_type)
        
    def __getitem(self, index: int):
        '''
            Parameters:
                index: Represents the index of an element in this grid
            Return:
                This function returns the element at the indicated index
        '''
        return self.data[index]
    
    def get_height(self) -> int:
        '''
            Return:
                This function returns the grid's height
        '''
        return self.data.size()
    
    def get_width(self,) -> int:
        '''
            Return:
                This function returns the grid's width
        '''
        return len(self.data[0])
    
    
    def __str__(self) -> str:
        '''
            Return:
                This function returns the string representation of this structure
        '''
        result = ""
        for row in range(self.data.size()):
            for column in range(self.get_width()):
                result += str(self.data[row][column]) + " "
            if row == self.data.size() - 1:
                continue
            else:
                result += "\n"
        return result