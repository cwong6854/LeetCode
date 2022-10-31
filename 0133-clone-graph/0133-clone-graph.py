"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # create copy and return clone from input -> node
        # bfs and hashmap
        # clone hashmap will track old and new nodes
        clone = {}
        
        def cloneNode(n):
            if n in clone:
                return clone[n]
            
            copy = Node(n.val)
            # track old and new node
            clone[n] = copy
            # create neighbors for clone
            for nbors in n.neighbors:
                copy.neighbors.append(cloneNode(nbors))
            return copy
        return cloneNode(node) if node else None
        
        
                
            
                
                
        
                 