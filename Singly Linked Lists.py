# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 08:10:14 2020

@author: Owner
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = Node(data)

        return None

    # Returns the length (integer) of the linked list.
    def length(self):
        cur_node = self.head
        ndx = 0

        while cur_node is not None:
            cur_node = cur_node.next
            ndx += 1

        return ndx

    # Print and return linked list in traditional Python list format.
    def to_list(self):
        cur_node = self.head
        lst = []

        while cur_node is not None:
            lst.append(cur_node.data)
            cur_node = cur_node.next

        print(lst)
        return lst

    # Print and return linked list in traditional Python dictionary format.
    def to_dict(self):
        cur_node = self.head
        ndx = 0
        dictionary = dict()

        while cur_node is not None:
            dictionary[ndx] = cur_node.data
            cur_node = cur_node.next
            ndx += 1
        print(dictionary)
        return dictionary

    # Return the value of the node at 'index'.
    def get_value(self, index):
        cur_node = self.head
        ndx = 0

        if index > self.length() - 1 or index < 0:
            print('Error: Index is out of range')
            return None

        while cur_node is not None:
            if index == ndx:
                print(cur_node.data)
                return cur_node.data
            cur_node = cur_node.next
            ndx += 1


    # Erase the node at index 'index'.
    def erase(self, index):
        cur_node = self.head
        ndx = 0

        if index > self.length() - 1 or index < 0:
            print('Error: Index is out of range')
            return None

        if index == 0:
            self.head = cur_node.next
            return None

        while cur_node is not None:
            if index == ndx + 1:
                cur_node.next = cur_node.next.next
            cur_node = cur_node.next
            ndx += 1
        return None

    # Allows for bracket operator syntax (i.e. a[0] to return first item).
    def __getitem__(self, index):
        return self.get_value(index)

    # Inserts a new node at index 'index' containing data 'data'.
    # Indices begin at 0. If the provided index is greater than or
    # equal to the length of the linked list the 'data' will be appended.
    def insert_data(self, index, data):
        cur_node = self.head
        ndx = 0
        node = Node(data)

        if index > self.length() or index < 0:
            print('Error: Index is out of range')
            return None

        if index == 0:
            self.head = node
            node.next = cur_node
            return None

        if index == self.length():
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = node
            return None

        while cur_node is not None:
            if index == ndx + 1:
                node.next = cur_node.next
                cur_node.next = node
                return None
            cur_node = cur_node.next
            ndx += 1


    # Insert the node 'node' at index 'index'. Indices begin at 0.
    # If the 'index' is greater than or equal to the length of the linked
    # list the 'node' will be appended.
    def insert_node(self, index, node):
        cur_node = self.head
        ndx = 0

        if type(node) is not Node:
            print('Error: Input is not of type Node')
            return None

        if index > self.length() or index < 0:
            print('Error: Index is out of range')
            return None

        if index == 0:
            self.head = node
            node.next = cur_node
            return None

        if index == self.length():
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = node
            return None

        while cur_node is not None:
            if index == ndx + 1:
                node.next = cur_node.next
                cur_node.next = node
            cur_node = cur_node.next
            ndx += 1
        return None

    # Update the data at index 'index' equal to 'data'.
    # Indices begin at 0. If the 'index' is greater than or equal
    # to the length of the linked list a warning will be printed
    # to the user.
    def update(self, index, data):
        cur_node = self.head
        ndx = 0

        if index > self.length() - 1 or index < 0:
            print('Error: Index out of range')
            return None

        while cur_node is not None:
            if index == ndx:
                cur_node.data = data
                return None
            ndx += 1
            cur_node = cur_node.next

    # Copy linked list to new linked list
    def clone(self, lst):
        self.head = Node(None)
        cur_node = self.head
        lst_node = lst.head

        while lst_node.next is not None:
            cur_node.data = lst_node.data
            cur_node.next = Node(None)
            cur_node = cur_node.next
            lst_node = lst_node.next
        cur_node.data = lst_node.data

    # You are given two non-empty linked lists representing two non-negative
    # integers. The digits are stored in reverse order and each of their nodes
    # contain a single digit. Add the two numbers and return it as a linked
    # list.
    # You may assume the two numbers do not contain any leading zero, except
    # the number 0 itself.

    def addTwoNumbers(self, l1, l2):
        self.head = Node(None)
        cur_node = self.head
        l1_node = l1.head
        l2_node = l2.head
        carry = 0

        while l1_node is not None or l2_node is not None:

            x1 = l1_node.data if l1_node is not None else 0
            x2 = l2_node.data if l2_node is not None else 0

            remain = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10

            cur_node.data = remain

            l1_node = l1_node.next if l1_node is not None else None
            l2_node = l2_node.next if l2_node is not None else None

            if l1_node is not None or l2_node is not None or carry != 0:
                cur_node.next = Node(None)

            cur_node = cur_node.next

        if carry > 0:
            cur_node.data = carry

        return None


print('\nCreate linked list with head and append')
L1 = LinkedList()
L1.head = Node(0)
L1.append(1)
L1.append(2)
L1.append(3)
L1.append(4)
L1.to_list()

print('\nPrint and return linked list as dictionary')
L1.to_dict()

print('\nPrint and return linked list as list')
L1.to_list()

print('\nReturn length of linked list ')
print('The length of linked list is: %d ' % L1.length())

print('\nAppend value to linked list')
L1.append(5)
L1.to_list()

print('\nGet value at index from linked list')
L1.get_value(5)

print('\nErase value at index from linked list')
L1.erase(5)
L1.to_list()

print('\nGet value at index from linked list using bracket operator')
L1[4]

print('\nInsert value at index to linked list')
L1.insert_data(3, 'monkey')
L1.to_list()
L1.erase(3)

print('\nInsert Node at index to linked list')
L1.insert_node(3, Node('monkey'))
L1.to_list()
L1.erase(3)

print('\nUpdate data at index to linked list')
L1.update(3, 'monkey')
L1.to_list()
L1.update(3, 3)

print('\nCopy linked list to new linked list')
L2 = LinkedList()
L2.clone(L1)
L2.to_list()

print('\nAdd Two Numbers represented as linked lists')
l1 = LinkedList()
l1.head = Node(9)
l1.append(9)
l1.append(9)
l1.to_list()

l2 = LinkedList()
l2.head = Node(9)
l2.append(9)
l2.to_list()

l0 = LinkedList()
l0.addTwoNumbers(l1, l2)
l0.to_list()
