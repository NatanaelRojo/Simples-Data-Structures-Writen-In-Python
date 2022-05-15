'''
    This file implements a double linked list data structure. This structure is based on double linked nodes
    A double linked list is a sequential and dynamic data structure. This structure can contain any number of elements
'''

from typing import Iterable
from ...Node.DLNode.double_node import T, DLNode


class DLList:
    '''
        This is the Double Linked List class
        This class implements the basics operations of a double linked list
    '''

    def __init__(self) -> None:
        '''
            This is the class constructor. This function initialize the class' attributes
        '''
        self.head: DLNode = None
        self.taill: DLNode = None
        self.__size: int = 0

    
    def append(self, data: T) -> None:
        '''
            Parameters:
                data: Represents the element to insert
            This function insert an element at the end of this structure and increments its size
        '''
        node = DLNode(data)

        if self.head == None and self.taill == None:
            self.head = node
            self.taill = node
            self.__size += 1
        else:
            current = self.taill
            self.taill = node
            self.taill.next = node.next
            self.taill.previous = current
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
            data = current.get_data()
            current = current.get_next()
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
                    self.head.previous = None
                    self.__size -= 1
                    return current.data
                elif current == self.taill:
                    self.taill = previous
                    self.taill.next = current.next
                    self.taill.previous = previous.previous
                    self.__size -= 1
                    return current.data
                else:
                    previous.next = current.next
                    current.next.previous = previous
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
        return None


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
            This function inserts an element at the begining of the list
        '''
        current = self.head
        self.head = DLNode(data)
        self.head.next = current
        self.head.previous = current.previous
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
        elif index == self.size() - 1:
            self.append(data)
            return True
        else:
            _index = 0
            current = self.head
            previous = self.head

            while _index <= index:
                if _index == index:
                    previous.next = DLNode(data)
                    previous.next.next = current
                    previous.next.previous = previous
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
                self.head.previous = None
                self.__size -= 1
                return True
        else:
            current = self.head
            previous = self.head
            _index = 0

            while _index <= index:
                if _index == index:
                    if _index == self.size() - 1:
                        self.taill = previous
                        self.taill.next = None
                        self.__size -= 1
                        return True
                    else:
                        previous.next = current.next
                        current.next.previous = previous
                        self.__size -= 1
                        return True
                previous = current
                current = current.next
                index += 1
            return False
                

    def clear(self) -> None:
        '''
            This function clear the list, that is, remove the all elements
        '''
        self.head = None
        self.taill = None
        self.size = 0
    

    def reverse(self) -> Iterable:
        '''
            This function returns a list with opposite order
        '''
        reverse_list = []
        current = self.taill

        while current:
            if current == self.head:
                reverse_list.append(current.data)
                break
            reverse_list.append(current.data)
            current = current.previous
        return reverse_list
    

    def __str__(self) -> str:
        '''
        Return:
            This function returns the string representation of this structure
        '''
        output = ''
        index = 0
        for i in self:
            if self.size() == index:
                output += str(i)
                break
            output += str(i) + '\n'
            index += 1
        return output