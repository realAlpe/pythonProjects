from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: 'TreeNode' = None
    right: 'TreeNode' = None


class Solution:
    """https://leetcode.com/problems/maximum-depth-of-binary-tree/"""

    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
