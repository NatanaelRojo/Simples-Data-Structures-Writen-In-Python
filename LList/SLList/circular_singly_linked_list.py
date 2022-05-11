"""
    This file implements a circular single linked list data structure
    This structure is based on simple nodes
"""

from .SLNode.single_node import Node


class CLList:
    def __init__(self) -> None:
        self.head = None
        self.taill = None
        self.__size = 0
    
    def append(self, data) -> None:
        node = Node(data)

        if self.head == None and self.taill == None:
            self.head = node
            self.taill = self.head
        else:
            self.taill.next = node
            self.taill = self.taill.next
            self.taill.next = self.head
        self.__size += 1
    

    def size(self) -> int:
        return self.__size
    

    def __iter__(self):
        current = self.head

        while current:
            if current == self.taill:
                data = current.data
                break
            data = current.data
            current = current.next
            yield data
        yield data
    
    def delete(self, data):
        current = self.head
        previous = self.head

        while current:
            if current.get_data() == data:
                if current == self.head:
                    self.head = self.head.next
                    self.taill = self.head
                elif current == self.taill:
                        previous.next = self.head
                        self.tail = previous
                        return current.data
                else:
                    previous.next = current.next
                self.__size -= 1
                return current.data
            previous = current
            current = current.next
    

    def search(self, data):
        for node in self:
            if node == data:
                return node


    def replace(self, value, new_value) -> bool:
        current = self.head

        while current:
            if current.data == value:
                current.data = new_value
                return True
            current = current.next
        return False


    def appbegin(self, value) -> None:
        current = self.head
        self.head = Node(value)
        self.head.next = current
        self.taill.next = self.head
    

    def insert(self, position, value) -> bool:
        if position == 0:
            self.appbegin(value)
            return True
        elif position == self.size() - 1:
            self.append(value)
            return True
        else:
            index = 0
            current = self.head
            previous = self.head

            while index <= position:
                if index == position:
                    previous.next = Node(value)
                    previous.next.next = current
                    return True
                index += 1
                previous = current
                current = current.next
        return False
    

    def pop(self, position):
        if position == 0:
            if self.size() == 1:
                self.clear()
            else:
                current = self.head
                self.head = self.head.next
                self.tail = self.head
                return True
        else:
            current = self.head
            previous = self.head
            index = 0

            while index <= position:
                if index == position:
                    if index == self.size() - 1:
                        self.taill = previous
                        self.taill.next = self.head
                        return True
                    else:
                        previous.next = current.next
                        return True
                previous = current
                current = current.next
                index += 1
            return False
                

    def clear(self):
        self.head = None
        self.taill = None
        self.size = 0
    

    def __str__(self) -> str:
        output = ''
        index = 0
        for i in self:
            if self.size() == index:
                output += str(i)
                break
            output += str(i) + '\n'
            index += 1
        return output