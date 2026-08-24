class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        oldToCopy = {}

        def dfs(curr):
            if curr in oldToCopy:
                return oldToCopy[curr]

            copy = Node(curr.val)
            oldToCopy[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)