class UF:
    def __init__(self, n):
        self.parent = []
        self.count = n
        self.size = []
        for i in range(n):
            self.parent[i] = 1
            self.size[i] = 1

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)
