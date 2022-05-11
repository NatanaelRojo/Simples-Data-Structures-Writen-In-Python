"""
    This files contains te implementation of a bidimentional array.
    This class is based on pPython lists.
"""

from .staticarray import Array


class Grid:
    
    def __init__(self, rows, columns, value_type=None) -> None:
        self.value_type = value_type
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, value_type)
        
    def __getitem(self, index):
        return self.data[index]
    
    
    def get_height(self) -> int:
        return self.data.size()
    
    def get_width(self,) -> int:
        return len(self.data[0])
    
    
    def __str__(self) -> str:
        result = ""
        for row in range(self.data.size()):
            for column in range(self.get_width()):
                result += str(self.data[row][column]) + " "
            if row == self.data.size() - 1:
                continue
            else:
                result += "\n"
        return result