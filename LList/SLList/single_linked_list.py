'''
    This file implements a single linked list data structure. This structure is based on singly linked nodes
    A singly linked list is a sequential and dynamic data structure. This structure can contain any number of elements
'''

from typing import Iterable, TypeVar, Generic

from ...Node.SLNode.single_node import T, SLNode

T = TypeVar('T')

class SLList(Generic[T]):
    '''
        This is the Singly Linked List class
        This class implements the basics operations of a singly linked list
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
            self.taill = node
        else:
            self.taill.next = node
            self.taill = self.taill.get_next()
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
                    self.__size -= 1
                    return current.data
                elif current == self.taill:
                    self.taill = previous
                    self.taill.next = current.next
                    return current.data
                else:
                    previous.next = current.next
                    self.__size -= 1
                    return current.data
            previous = current
            current = current.next
        return None
    
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
        self.head = SLNode(data)
        self.head.next = current
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
                    previous.next = SLNode(data)
                    previous.next.next = current
                    self.__size += 1
                    return True
                _index += 1
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
        if position == 0:
            if self.size() == 1:
                current = self.head.data
                self.clear()
                return current
            else:
                current = self.head
                self.head = self.head.next
                return current.data
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
                        return current.data
                    else:
                        previous.next = current.next
                        self.__size -= 1
                        return current.data
                previous = current
                current = current.next
                index += 1
            return None
                

    def clear(self) -> None:
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
            if self.size() - 1== index:
                output += str(i)
                break
            output += str(i) + '\n'
            index += 1
        return output