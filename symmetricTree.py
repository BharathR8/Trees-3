#Time Complexity:O(n)
#Space Complexity:O(1)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)

class Solution:

    def isSymmetric(self, root):

        if (root == None):
            return True;

        stack = []
      
        def dfs(left, right):

            if (left == None and right == None):
                return True
            
            if(left == None or right == None):
                return False
            
            if(left.val != right.val):
                return False
            
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        

        return dfs(root.left, root.right)



result = Solution()
output = result.isSymmetric(root)
print(output)




