from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: 'TreeNode' = None
    right: 'TreeNode' = None


class Solution:
    """https://leetcode.com/problems/invert-binary-tree/"""

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root:
            return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
        return None
