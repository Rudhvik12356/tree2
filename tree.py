class TreeNode():
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
#Starts with the left of left subtrre making it a root
#Back to the left subtree root node and then to hte right of subtree node
#Then it would got back to orignal node
#It would go left of of right subtee and would do the same until the tree is finished
def inorderTraversal(root):
    if root.leftNode != None:
        inorderTraversal(root.leftNode)
        
    print(root.value)

    if root.rightNode != None:
        inorderTraversal(root.rightNode)
#Preorder travesal goes form root node to left subtree nopde and then to right subtree node and continiues
def preorderTraversal(root):
    print(root.value)
    if root.leftNode is not None:
        preorderTraversal(root.leftNode)
    if root.rightNode is not None:
        preorderTraversal(root.rightNode)    
    
root = TreeNode(15)
root.leftNode = TreeNode(7)
root.rightNode = TreeNode(20)
root.leftNode.leftNode = TreeNode(4)
root.rightNode.rightNode = TreeNode(25)
root.leftNode.rightNode = TreeNode(10)
root.rightNode.leftNode = TreeNode(17)

inorderTraversal(root)
preorderTraversal(root)

# #HW Practice 1: Count the NodesTask: Create a function to count the total number of nodes present in a given TreeNode.
# Input: A TreeNode with a root node (e.g., Root=10, Left=5, Right=15).
# Goal: Output: 3.
# Logic (Give If Needed):
# Base Case: If root is None, return 0.
# Recursive Step: Return 1 + count_nodes(root.left) + count_nodes(root.right). This adds the current node (1) to the total nodes found in the left and right subTreeNodes.
# Practice 2: Find the Maximum Value
# Task: Find the largest integer value stored in a binary TreeNode.
# Input: A TreeNode with various integer values (e.g., 10, 20, 5).
# Goal: Output: 20.
# Logic (Give If Needed):
# Base Case: If root is None, return a very small number (e.g., -1000).
# Recursive Step: Find the max in the left child and the max in the right child.
# Compare root.data, left_max, and right_max and return the highest of the three.