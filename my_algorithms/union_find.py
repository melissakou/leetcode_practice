class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, node):
        while self.parent[node] != node: node = self.parent[node]
        return node

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            self.parent[root1] = root2