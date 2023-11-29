from PriorityQueue_Interface import PriorityQueue_Interface


class TwoDSequencePQ(PriorityQueue_Interface):
    def __init__(self):
        self.pq = []
        self.length = 0

    def add(self, priority, item):
        while len(self.pq) <= priority:
            self.pq.append([])
        self.pq[priority].append(item)
        self.length += 1

    def min(self):
        for i, row in enumerate(self.pq):
            if row:
                return i, row[0]
        return None, None

    def remove_min(self):
        for i, row in enumerate(self.pq):
            if row:
                item = row.pop(0)
                self.length -= 1
                if not row:
                    del self.pq[i]
                return i, item
        return None, None

    def is_empty(self):
        return self.length == 0

    def __len__(self):
        return self.length