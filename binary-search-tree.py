'''

    A binary tree implemented in by Kaled Brahmi

'''
import random

# CHANGE THIS
NUM = 10 # Number of values in the tree
MIN_NUM = 1 # Minimum value of the range for the randint function
MAX_NUM = 100 # Maximum value of the range for the randint function


# Node class that contains the value and the references to the right and left nodes
class Node:
    def __init__(self, value, right, left):
        self.value = value
        self.right = right
        self.left = left


# The addNode function is a recursive function that takes two arguments, the current head that 
# will change for each call of the function and a value for the new node to add to the tree

def addNode(head, value):
    # Base case (end of the tree)
    if head == None:
        return
    # Go right because the value to add is bigger than the current node
    if value > head.value:
        if head.right == None:
            head.right = Node(value, None, None)
            return
        addNode(head.right, value)
        return
    # Go left because the value to add is smaller than the current node
    if value < head.value:
        if head.left == None:
            head.left = Node(value, None, None)
            return
        addNode(head.left, value)
        return
    # The node with the value you want to add is already present in the tree
    else:
        return

# Recursive function that deletes a node from the tree. Return boolean (true if removed ; false if is not removed)
def removeNode(head, value):
    # Base case: end of the tree and node not found
    if head == None:
        return False
    
    # If the value if equal to the current node it will be removed
    if value == head.value:
        # The node to remove have a left reference different from 'None' so it reference a real node
        if head.left != None:
            tempNodeLeft = head.left
            tempNodeLeft2 = head

            # Iterates untill it finds the greates value on the right of the Node to remove
            while tempNodeLeft.right != None:
                tempNodeLeft2 = tempNodeLeft
                tempNodeLeft = tempNodeLeft.right
            # Check if the value that will take the place of the one to remove have a valid reference on the left
            if tempNodeLeft.left != None:
                head.value = tempNodeLeft.value
                tempNodeLeft.value = tempNodeLeft.left.value
                tempNodeLeft.left = tempNodeLeft.left.left
                tempNodeLeft.right = tempNodeLeft.left.right
            else:
                head.value = tempNodeLeft.value
                tempNode2Left.right = None
        # The node to remove have a valid node on the right
        elif head.right != None:
            tempNodeRight = head.right
            tempNodeRight2 = head
            # Iterates untill it finds the lowest value on the left of the Node to remove
            while tempNodeRight.left != None:
                tempNodeRight2 = tempNodeRight
                tempNodeRight = tempNodeRight.left
            # Check if the value that will take the place of the one to remove have a valid reverence on the right
            if tempNodeRight.right != None:
                head.value = tempNodeRight.value
                tempNodeRight.value = tempNodeRight.right.value
                tempNodeRight.left = tempNodeRight.right.left
                tempNodeRight.right = tempNodeRight.right.right
            else:
                head.value = tempNodeRight.value
                tempNodeRight2.left = None
        # The node to remove is the last node of the tree
        else:
            head.value = None

        return True

    # If the value is greater than the value of the current node the program will search for it in the right part of the tree 
    # by recursively calling the 'removeNode' function
    elif value > head.value:
        return removeNode(head.right, value)
    
    # The value is less than the value of the head so the program will search in the left part of the tree
    else:
        return removeNode(head.left, value)

# Recursive function that check if a value is present in the tree
def findNode(head, value):
    # Base case: if the end of the tree is reached without finding the value the program will return false (not find)
    if head == None:
        return False

    # If the value is equal to the value of the present node the program will return true (find)
    elif head.value == value:
        return True
    
    # The value is less than the node so it should be on the left
    elif head.value > value:
        return findNode(head.left, value)

    # The value is greater than the node so it should be on the right
    else:
        return findNode(head.right, value)

# Recursive function that prints the values of the tree in order
def printTree(head):
    # Base case (end of the tree)
    if head == None:
        return
    printTree(head.left)  # Print the left part repectively to the current node
    print(head.value)     # Print the current node
    printTree(head.right) # Print the right part respectively to the current node


def main():
    # Creating the head node with the right and left hands equals to None
    head = Node(random.randint(MIN_NUM, MAX_NUM), None, None)
    # For loop that populates the tree with NUM random values from MIN_NUM to MAX_NUM
    for i in range(1, NUM-1):
        addNode(head, random.randint(MIN_NUM, MAX_NUM))
    
    # Print the tree in order
    printTree(head)

if __name__ == "__main__":
    main()


