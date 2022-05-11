"""
    This is a basic implementation of an Array data structure.
    This implementation is based on Python lists.
"""


class Array:

    def __init__(self, capacity, fill_value=None) -> None:
        self.items = [fill_value for i in range(capacity)]

    def size(self) -> int:
        return len(self.items)
    
    def get_item(self, index):
        return self.items[index]
    
    def set_item(self, index, new_item) -> None:
        self.items[index] = value
    
    def __str__(self) -> str:
        return str(self.items)
    
    def __iter__(self) -> iter:
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item) -> None:
        self.items[index] = new_item
    
    def __len__(self):
        return len(self.items)