from collections import Counter, defaultdict

class QuickFind:
    def __init__(self, size):
        self._arr = [i for i in range(size)]

    def are_connected(self, p1, p2):
        return self._arr[p1] == self._arr[p2]

    def union(self, p1, p2):
        p1_id = self._arr[p1]
        p2_id = self._arr[p2]

        for index, element in enumerate(self._arr):
            if element == p1_id:
                self._arr[index] = p2_id

    def elements_groups(self):
        return self._arr

class QuickUnion:
    def __init__(self, size):
        self._arr = [i for i in range(size)]
        self.size = size

    def root(self, element):
        while(element != self._arr[element]):
            element = self._arr[element]
        return element

    def union(self, p1, p2):
        p1_root = self.root(p1)
        p2_root = self.root(p2)

        self._arr[p2_root] = p1_root

    def elements_groups(self):
        return [self.root(e) for e in self._arr]

    def are_connected(self, p1, p2):
        return self.root(p1) == self.root(p2)

arr = [
	[0, 2],
	[1, 8],
	[1, 4],
	[2, 8],
	[2, 6],
	[3, 5],
	[6, 9],
]


a = QuickFind(10)

for i, j in arr:
    a.union(i, j)

elements = a.elements_groups()
print(sum(1 for i in range(10) for j in range(i + 1, 10) if elements[i] != elements[j]))
