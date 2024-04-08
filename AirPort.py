"""
Airport class for letting planes land wait and take off and saving data related to them in the system
"""
class AirPort:
    def __init__(self,plane):
        self.plane = plane

    """
    Function to print the output
    """

    def output(self,binaryTree, hashT, name, state):
        # Arrive Output
        print()
        size = binaryTree.getSize(binaryTree.getRoot())  # size of binary tree
        arrayTree = binaryTree.returnValueArray()  # array of values from binary tree
        arrayEvents = state.returnValueArray()  # returns array of states

        # prints arriving in order that happened today
        spotNum = 0
        while spotNum < size:
            currentVal = hashT.find(arrayTree[spotNum])
            if spotNum == 0:
                print(f"Planes {name} In Order Event {arrayEvents[spotNum]}------------\n")
                print(f"Plane Number {spotNum} of the day", currentVal)
            else:
                print(f"Plane Number {spotNum} of the day", currentVal)
            spotNum += 1

    """
    Check if any planes are waiting to land and if spots are open return 0 or 1
    """
    def checkForPlanes(self,terminalStack):
        # Adds to plane to terminal or denies and pusehes back into the air
        size = terminalStack.size()
        if terminalStack.isEmpty() or size <= 3:
            print("Spots are open land please")
            return 1
        return 0

    """
    Terminal and its logic
    """

"""
Part of binary tree to help it function
"""
class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

"""
Binary tree data structure for storage
"""
class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.__root = None

    def getRoot(self):
        return self.__root

    @staticmethod
    def getSize(root):
        if root is None:
            return 0
        return 1 + BinaryTree.getSize(root.left) + BinaryTree.getSize(root.right)

    def isEmpty(self):
        return self.__root is None

    def __insert(self, value, node):
        if node is None:
            node = TreeNode(value)
        elif value < node.data:
            node.left = self.__insert(value, node.left)
        elif value > node.data:
            node.right = self.__insert(value, node.right)

        return node

    def insert(self, value):
        self.__root = self.__insert(value, self.__root)

    def __inorder(self, node, result):
        if node is not None:
            self.__inorder(node.left, result)
            result.append(node.data)
            self.__inorder(node.right, result)

    #returns all the values as array
    def returnValueArray(self):
        result = []
        self.__inorder(self.__root, result)
        return result



"""
Hash function data structure
"""
class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__data = [None] * size
        for i in range(size):
            self.__data[i] = []

    def returnSelfData(self):
        return self.__data


    def hash(self, key):
        total = 0
        for c in key:
            total += ord(c)
        total %= self.__size

        return total

    def insert(self, plane):
        hashcode = self.hash(plane.flightNo)
        self.__data[hashcode].append(plane)
        #print("Inserted", plane, "at", hashcode)

    def find(self, key):
        hashcode = self.hash(key)
        for plane in self.__data[hashcode]:
            if plane.flightNo == key:
                return plane
        return None

    def __str__(self):
        output = ""
        for i in range(len(self.__data)):
            output += str(i) + " "
            for person in self.__data[i]:
                output += person.__str__() + " -- "
            output += "\n"
        return output


"""
List stack for first in first out behaviour terminal
"""
class ListStack:
    def __init__(self):
        self.__data = []

    def isEmpty(self):
        return len(self.__data) == 0

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        del self.__data[-1]

    def peek(self):
        return self.__data[-1]

    def size(self):
        return len(self.__data)

    def popBottom(self):
        if not self.isEmpty():
            del self.__data[0]

    def peekBottom(self):
        re = self.__data[0] if self.__data else None  # Return None if the stack is empty
        return re

    def __str__(self):
        return self.__data.__str__()
