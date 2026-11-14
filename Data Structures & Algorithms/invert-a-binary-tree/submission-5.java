/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode invertTree(TreeNode root) {
        
        Stack<TreeNode> s = new Stack<>();

        s.push(root);

        while (!s.isEmpty()) {
            TreeNode cur = s.pop();
            if (cur == null) continue;
            TreeNode t = cur.left;
            cur.left = cur.right;
            cur.right = t;

            s.push(cur.left);
            s.push(cur.right);
        }

        return root;
    }
}
