"""
Dynamic Array
Linked List
Stack & Queue
Hash Tables
Binary Search Tree
Binary Heaps & Priority Queue
Graphs
Trie
"""

"""
1. Dynamic Array:
    - Similiar to an array, but with difference that its size 
      can be dynamically modified at runtime.
    - 
"""

"""
class M(object):

    def public(self):
        print("Use Tab to see me!")

    def _private(self):
        print("You won't be able to Tab to see me!")


m = M()
m.public()
m._private()
"""

import ctypes
class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python list)
    '''

    def __init__(self):
        self.n = 0 # count number of elements (default 0)
        self.capacity = 1 # default capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # check if k index is in bounds of array
            return IndexError('K is out of bounds!')

        return self.A[k] # Retrieve from the array at index k


    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            # double capacity if not enough room
            self._resize(2 * self.capacity)

        self.A[self.n] = ele # Set self.n index to element
        self.n += 1

        def insertAt(self, item, index):
            """
            This function inserts the item at any specified index
            """

            if index < 0 or index > self.n:
                print("Please enter appropriate index...")
                return
            
            if self.n == self.capacity:
                self._resize(2*self.capacity)

            for i in range(self.n-1, index-1, -1):
                self.A[i+1] = self.A[i]

            self.A[index]=item
            self.n += 1


    def delete(self):
        """
        Function deletes item from the end of array
        """
        if self.n == 0:
            print("Array is empty, deletion not possible")
            return

        self.A[self.n-1] = 0
        self.n = 1

    def removeAt(self, index):
        """
        Function deletes item from a specified index
        """

        if self.n == 0:
            print("Array is empty, deletion not possible")
            return
        
        if index < 0 or index >= self.n:
            return IndexError("Index out of bound ... deletion not possible")
        
        if index == self.n-1:
            self.A[index] = 0
            self.n -= 1
            return
        
        for i in range(index, self.n-1):
            self.A[i] = self.A[i+1]

        self.A[self.n-1] = 0
        self.n -= 1

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """

        B = self.make_array(new_cap) # New bigger array

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B # Call A to the new bigger array
        self.capacity = new_cap # Reset the capacity

    
    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """

        return (new_cap * ctypes.py_object)()


#Instantiate:
arr = DynamicArray()

# Append new element
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))
print(arr[0])