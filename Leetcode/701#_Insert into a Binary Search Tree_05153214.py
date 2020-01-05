class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node=TreeNode(val)
        if root.val==None:      
            root.val=val      

        else:
            if val <= root.val:          
                if root.left == None:
                    root.left = new_node
                else:
                    self.insertIntoBST(root.left,val)

            elif val > root.val:        
                if root.right == None:
                    root.right = new_node
                else:
                    self.insertIntoBST(root.right,val)
            return root
        


