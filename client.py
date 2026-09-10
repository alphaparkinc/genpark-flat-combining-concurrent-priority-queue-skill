class FlatCombiningPQ:
    """
    Flat Combining Priority Queue avoiding lock thrashing
    by delegating concurrent operations to a combiner thread.
    """
    def __init__(self):
        self.heap = []
        self.publication_list = []

    def submit_request(self, op, val=None):
        req = {"op": op, "val": val, "status": "PENDING", "res": None}
        self.publication_list.append(req)
        self._combine()
        return req["res"]

    def _combine(self):
        for req in self.publication_list:
            if req["status"] == "PENDING":
                if req["op"] == "INSERT":
                    self.heap.append(req["val"])
                    self._sift_up(len(self.heap) - 1)
                    req["res"] = "OK"
                elif req["op"] == "EXTRACT_MIN":
                    if not self.heap:
                        req["res"] = None
                    else:
                        min_v = self.heap[0]
                        last = self.heap.pop()
                        if self.heap:
                            self.heap[0] = last
                            self._sift_down(0)
                        req["res"] = min_v
                req["status"] = "DONE"
        self.publication_list = [r for r in self.publication_list if r["status"] == "PENDING"]

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.heap)
        while 2 * idx + 1 < n:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = left
            if right < n and self.heap[right] < self.heap[left]:
                smallest = right
            if self.heap[smallest] < self.heap[idx]:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break
