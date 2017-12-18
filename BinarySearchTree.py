"""
 In order to insert a new node ..
 
 1. If Current node doesn't have a left_child, we just
 create a new node and set it to the current node's left_child. 

 2. If it does have a left_child, we create a new node and put it
 in the current left child's place. Allocate this left child node to the new
 node's left child. 
"""  
class BinaryTree:
    
    
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
 
    def insert_left(self,value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
    def insert_right(self,value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
    #=====# DEPTH FIRST SEARCH #====#
    """                    1     # Level/Depth 0:  1 Node value 1
                      /  \
                     2    5  #Level/Depth  1:  nodes with values 2, 5
                    / \   / \
                   3   4  6  7 #Level/Depth 2: nodes with values 3,4,6,7"""
                   
    def pre_order(self): # prints 1,2,3,4,5,6,7
        print(self.value)
        
        if self.left_child:
            self.left_child.pre_order()
            
        if self.right_child:
            self.right_child.pre_order()
            
        # 1. Print the value of the node.
        # 2. Go to left child print.
        # 3. Go to right child and print. IFF they have 'em.
            
    def in_order(self):   # Prints 3,2,4,1,6,5,7
        # 1. Go to left child and print it. IFF it has a left child
        #Print node's value.
        #. Go to right child and print it. 
        if self.left_child:
            self.left_child.in_order()
            
        print(self.value)
        
        if self.right_child:
            self.right_child.in_order()
            
    def post_order(self):  #Prints 3,4,2,6,7,5,1
        #Left first, right second, middle last.
        if self.left_child:
            self.left_child.post_order()
            
        if self.right_child:
            self.right_child.post_order()
        
        
        print(self.value)
        # Go to left child and print
        # Go to right child and print 
        # 3. Print the node's value.
        
    # ====== Breadth First Search =======#
    # Level by Level, Depth by Depth 
    """                1     # Level/Depth 0:  1 Node value 1
                      /  \
                     2    5  #Level/Depth  1:  nodes with values 2, 5
                    / \   / \
                   3   4  6  7 #Level/Depth 2: nodes with values 3,4,6,7
    
    """
    # prints 1,2,5,3,4,6,7
    def bfs(self):  #Breadth first Search
        queue = Queue()
        queue.put(self)
        
        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)
            
            if current_node.left_child:
                queue.put(current_node.left_child)
                
            if current_node.right_child:
                queue.put(current_node.right_child)
                # Using Queue as data structure to help us
        # 1. Add the root not into the queue with the put method
        # 2. Iterate while queue is not empty.
        # 3. Get the first node in the queue, and print its value
        # 4. Add both left and right children into queue (if it has)
        # 5. Done. We Print the value of each node, level by level with
        # our queue.
        """
 DFS - Starts at root and explores as far as possible along
 each branch before backtracking.
 
 BFS - Starts at root and explores the neighbor nodes first
 before moving to the nex level neighbors. 
 """
        
    """ ##### ======== Binary Search Tree ======= ##### 
    
     - Ordered or Sorted Binary Trees,
     and it keeps its values in sorted order, so
     that lookup and other operations can use
     the principle of binary search. 
    
    BST - the value of a binary search tree node is larger
    than the value of the offspring of its
    left child, but smaller than the value of the offspring
    of its right child.
    """
    
    # imagine we have an empty tree and we want to add
    # nodes in this order: 50, 76, 21, 4, 32, 100, 64, 52. 
    
# 76 is greater than 50, so 76 goes on right side.
# 21 is smaller than 50, 21 goes left.
# 4 is smaller than 50, 50 has left-child 21. 4 is smaller than 21, goes on left
# side of 21.
# - 32 is smaller than 50. 50 has left child, 21. 32 is greater insert it on right side
# of 21. 
# - 100 is greater than 50. 50 has right child 76. insert 100 on right side of 76.
# - 64 greater then 50. 50 has right child 76. 64 is less than 76. It is left child of 76. 
# 52 is greater than 50. 50 has right child 76.
# 52 is smaller than 76. 76 has left child 64. 52 is smaller
# so insert 54 on left side of 64 node. 
    
class BinarySearchTree:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None
        
    def insert_node(self,value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value) #Recursive L-R Child
        elif value <= self.value:
            self.left_child = BinarySearchTree(value) #insert child
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value) #Recursive L-R Child
        else:
            self.right_child = BinarySearchTree(value) #insert child
    # We start with root node as our current node.
    # If value is smaller go to left subtree.
    #IF greater go to right subtree.
    # If both false, compare current node value and
    # the given value and if they are equal. 
    #If true it is there, if not, it is not in tree. 
    def find_node(self,value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)
        
        return value == self.value
    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None
    def find_minimum_value(self): # GO way down to left, if no nodes, we found smallest!
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value
    
    # DELETION.. Scenario 1, node with no children
    
    #   |50|                              |50|
#      /      \                           /    \
#    |30|     |70|   (DELETE 20) --->   |30|   |70|
#   /    \                                \
# |20|   |40|                             |40|

# Scenario 2. Node with 1 child. 

#        |50|                              |50|
#      /      \                           /    \
#    |30|     |70|   (DELETE 30) --->   |20|   |70|
#   /            
# |20|

# Scenario 3. A node with 2  children

#        |50|                              |50|
#      /      \                           /    \
#    |30|     |70|   (DELETE 30) --->   |40|   |70|
#   /    \                             /
# |20|   |40|                        |20|
    def remove_node(self,value,parent):                                         #1
        if value < self.value and self.left_child:                              #2
            return self.left_child.remove_node(value,self)                      #3
        elif value < self.value:                                                #4
            return False                                                        #5
        elif value > self.value and self.right_child:                           #6
            return self.right_child.remove_node(value,self)                     #7
        elif value > self.value:                                                #8
            return False                                                        #9
        else:                                                                   #10
            if self.left_child is None and self.right_child is None and self == parent.left_child:   #11
                parent.left_child = None                                                             #12
                self.clear_node()                                                                    #13
            elif self.left_child is None and self.right_child is None and self == parent.right_child:  #14
                parent.right_child = None                                                             #15
                self.clear_node()                                                                    #16
            elif self.left_child and self.right_child is None and self == parent.left_child:        #17
                parent.left_child = self.left_child                                                 #18
                self.clear_node()                                                                  #19
            elif self.left_child and self.right_child is None and self == parent.right_child:      #20
                parent.right_child = self.left_child                                               #21
                self.clear_node()                                                                  #22
            elif self.right_child and self.left_child is None and self == parent.left_child:       #23
                parent.left_child = self.right_child                                               #24
                self.clear_node()                                                                  #25
            elif self.right_child and self.left_child is None and self == parent.right_child:     #26
                parent.right_child = self.right_child                                             #27
                self.clear_node()                                                                 #28
            else:                                                                                 #29
                self.value = self.right_child.find_minimum_value()                                 #30
                self.right_child.remove_node(self.value, self)                                    #31
                                                                                                   #32
            return True                                                                           #33
    
    """
    1. First: Note the parameters value and parent. We want to find the node that
    has this value  and the node's parent is important to the removal of the node.
    2. Second: Note the returning value. Our algorithm will return a boolean value. 
    It returns True if it finds the node and removes it. O.wise it returns False.
    
    3. From line 2 to line 9: We start searching for the node that has the value
    that we are looking for. If the value is smaller than the current nodevalue, we go to
    the left subtree, recursively IFF it has left child. If value is greater,
    go to the right subtree, recursively. 
    
    4. Line 10. We start to think about the remove algorithm. 
    5. Line 11 to 13: We cover the node with no children. And it is the left child
    of its parent. We remove the node by setting the parent's left child to None.
    6. Lines 14 and 15: We cover the node with no children, and it the right child from
    its parent. We remove the node by setting the parent's right child to None.
    7. Clear node method: Sets left and right child and value to None. 
    8. Line 16-18: We cover the node with just one child (left child)
    and its the left child from it's parent. We set the parents left child to the node's left
    child (the only child it has.)
    9. Lines 19 to 21: We cover the node with just one child (left child) and it is
    the right child from its parent. We set the parents right child to the node's
    left child (the only child it has.)
    10. Line 22-24: We cover the node wth just one child(right child)
    and it is the left child from its parent. We set the parent's left child to
    the node's right child (the only child it has.)
    11. line 25-27: We cover node with 1 child (right child.) nd it is the right 
    child from its parent. We set the parent's right child to the node's right child
    (the only child it has.)
    12. Line 28-30, we cover node with both left & right child. We get the node
    with the smallest value and set it to the value of the current node.
    Finish it by removing the smallest node. 
    13. Line 32: If we find the node we are looking for,return True,
    From line 11 to line 31 we handle this case. 
    """
    
    
    
bst = BinarySearchTree(15)  # initilaizing root = 15. 
bst.insert_node(10)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)

print(bst.find_node(15))  # True
print(bst.find_node(10))  # True
print(bst.find_node(3))   # false

            

        
#tree = BinaryTree('a')
#
#print(tree.value)  # a 
#print(tree.left_child) # None
#print(tree.right_child) # None
#a_node = BinaryTree('a')
#a_node.insert_left('b')
#a_node.insert_right('c')
#
#b_node = a_node.left_child
#b_node.insert_right('d')
#
#c_node = a_node.right_child
#c_node.insert_left('e')
#c_node.insert_right('f')
#
#d_node = b_node.right_child
#e_node = c_node.left_child
#f_node = c_node.right_child
#
#print(a_node.value) # a
#print(b_node.value) # b
#print(c_node.value) # c
#print(d_node.value) # d
#print(e_node.value) # e
#print(f_node.value) # f
