"""
    This file implements a circular singly linked list data structure. This structure is based on singly linked nodes
    A circular singly list is a sequential data structure.
    Where the next element of last node is the first element in the structure
"""


from typing import Iterable
from ...Node.SLNode.single_node import T, SLNode


class CLList:
    '''
        This is the Circular Singly Linked List class
        This class implements the basics operations of a circular singly linked list
    '''
    def __init__(self) -> None:
        '''
            This is the class constructor. This function initialize the class' attributes
        '''
        self.head: SLNode = None
        self.taill: SLNode = None
        self.__size: int = 0
    
    def append(self, data: T) -> None:
        '''
            Parameters:
                data: Represents the element to insert
            This function insert an element at the end of this structure and increments its size
        '''
        node = SLNode(data)

        if self.head == None and self.taill == None:
            self.head = node
            self.taill = self.head
            self.__size += 1
        else:
            self.taill.next = node
            self.taill = self.taill.next
            self.taill.next = self.head
        self.__size += 1
    

    def size(self) -> int:
        '''
            Return:
                This function returns the size of this structure, that is, the number of elements
        '''
        return self.__size
    

    def __iter__(self) -> Iterable:
        '''
            Return:
                This function returns the iterator of this structure
        '''
        current = self.head

        while current:
            if current == self.taill:
                data = current.data
                break
            data = current.data
            current = current.next
            yield data
        yield data
    
    def delete(self, data: T) -> T:
        '''
            Parameters:
                data: Represents the element to remove
            Return:
                This function returns the removed element
        '''
        current = self.head
        previous = self.head

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = self.head.next
                    self.taill = self.head
                    self.__size -= 1
                    return current.data
                elif current == self.taill:
                        previous.next = self.head
                        self.tail = previous
                        self.__size -= 1
                        return current.data
                else:
                    previous.next = current.next
                self.__size -= 1
                return current.data
            previous = current
            current = current.next
    

    def search(self, data: T) -> T:
        '''
            Parameters:
                data: Represents the element to search
            Return:
                This function returns the indicated element in parameters,
                if it is in the list, otherwise, returns None
        '''
        for node in self:
            if node == data:
                return node


    def replace(self, data: T, new_data: T) -> bool:
        '''
            Parameters:
                data: Represents the element to search
                new_data: Represents the element to replace
            Return:
                This function returns True if the element was replaced, otherwise, returns False
        '''
        current = self.head

        while current:
            if current.data == data:
                current.data = new_data
                return True
            current = current.next
        return False


    def appbegin(self, data: T) -> None:
        '''
            Parameters:
                data: Represents the element to insert
            This function inserts an element at the begining  of the list
        '''
        current = self.head
        self.head = SLNode(data)
        self.head.next = current
        self.taill.next = self.head
        self.__size += 1
    

    def insert(self, index: int, data: T) -> bool:
        '''
            Parameters:
                index: Represents the index where the element will be inserted
                data: Represents the element to insert
            Return:
                This function returns True if the element was inserted, otherwise, returns False
        '''
        if index == 0:
            self.appbegin(data)
            return True
        elif position == self.size() - 1:
            self.append(data)
            return True
        else:
            _index = 0
            current = self.head
            previous = self.head

            while _index <= index:
                if _index == index:
                    previous.next = SLNode(value)
                    previous.next.next = current
                    self.__size += 1
                    return True
                index += 1
                previous = current
                current = current.next
        return False
    

    def pop(self, index: int) -> T:
        '''
            Parameters:
                index: Represents the index to remove
            Return:
                This function returns the removed element.
                If the element is in the list, returns the element, otherwise, returns None
        '''
        if index == 0:
            if self.size() == 1:
                self.clear()
            else:
                current = self.head
                self.head = self.head.next
                self.tail = self.head
                self.__size -= 1
                return True
        else:
            current = self.head
            previous = self.head
            _index = 0

            while _index <= index:
                if _index == index:
                    if index == self.size() - 1:
                        self.taill = previous
                        self.taill.next = self.head
                        self.__size -= 1
                        return True
                    else:
                        previous.next = current.next
                        self.__size -= 1
                        return True
                previous = current
                current = current.next
                index += 1
            return False
                

    def clear(self):
        '''
            This function clear the list, that is, remove the all elements
        '''
        self.head = None
        self.taill = None
        self.size = 0
    

    def __str__(self) -> str:
        '''
        Return:
            This function returns the string representation of this structure
        '''
        output = ''
        index = 0
        for i in self:
            if self.size() - 1 == index:
                output += str(i)
                break
            output += str(i) + '\n'
            index += 1
        return output