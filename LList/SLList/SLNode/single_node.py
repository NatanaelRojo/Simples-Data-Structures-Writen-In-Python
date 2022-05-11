class Node:
    
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
