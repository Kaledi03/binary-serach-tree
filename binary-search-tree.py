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


