from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: 'TreeNode' = None
    right: 'TreeNode' = None


class Solution:
    """https://leetcode.com/problems/diameter-of-binary-tree/"""

    def __init__(self):
        self.diameter = 0

    def depth(self, node: TreeNode | None) -> int:
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        if left + right > self.diameter:
            self.diameter = left + right
        return 1 + (left if left > right else right)

    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        self.depth(root)
        return self.diameter
