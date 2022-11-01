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
        # create helper function that returns cloned node, along with its neighbors and other nodes
        # recursive and hashmap
        # store old and new nodes
        cloned = {}
        def cloning(node):
            # check if node is already in cloned, otherwise make copy and store
            if node in cloned:
                return cloned[node]
            
            copy = Node(node.val)
            cloned[node] = copy
            #check for neighbors, if there are neighbors then we recursive to check if neighbor exists, otherwise create a clone
            for n in node.neighbors:
                copy.neighbors.append(cloning(n))
            return copy
        return cloning(node) if node else None
    # runtime -> o(V+E): V -> vertices, E -> edges --> o(n)
                