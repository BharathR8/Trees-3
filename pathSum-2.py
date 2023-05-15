#Time Complexity: O(n)
#Space Complexity: O(n)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
root.right.left = TreeNode(13)


class Solution:

    def pathSum(self, root, targetSum):

        if (root == None):
            return []
        
        global res
        res = []

        def dfs(root, path):

            if (root == None):
                return
            

            if (root.left == None and root.right == None):
                path = path+[root.val]
                if(sum(path) == targetSum):
                    res.append(path)

            dfs(root.left, path+[root.val])
            dfs(root.right, path+[root.val])

        dfs(root, [])

        return res

targetSum = 22
res = Solution()
output = res.pathSum(root, targetSum)
print(output)