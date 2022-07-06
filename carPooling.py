class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nodes = []
        for passengers, from_idx, to_idx in trips:
            nodes.append((passengers, from_idx))
            nodes.append((-1*passengers, to_idx))

        nodes.sort(key=lambda x: x[-1])

        totalPassengers = 0
        i = 0
        while i < len(nodes):
            currIdx = nodes[i][1]
            while i < len(nodes) and nodes[i][1] == currIdx:
                totalPassengers += nodes[i][0]
                i += 1
            if totalPassengers > capacity:
                return False

        return True
