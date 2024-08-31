class MinHeap:
    def __init__(self):
        self.heap = []
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def get_parent_index(self, index):
        return (index - 1) // 2
    
    def get_left_child_index(self, index):
        return (2 * index) + 1
    
    def get_right_child_index(self, index):
        return (2 * index) + 2
    
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0
    
    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)
    
    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def heapify_up(self, index):
        while self.has_parent(index) and self.heap[index] < self.heap[self.get_parent_index(index)]:
            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)
            index = parent_index
    
    def heapify_down(self, index):
        while self.has_left_child(index):
            smallest_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.heap[self.get_right_child_index(index)] < self.heap[smallest_child_index]:
                smallest_child_index = self.get_right_child_index(index)
            
            if self.heap[index] < self.heap[smallest_child_index]:
                break
            
            self.swap(index, smallest_child_index)
            index = smallest_child_index
    
    def add(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)
    
    def remove_min(self):
        if self.is_empty():
            raise IndexError("Heap is empty.")
        
        min_item = self.heap[0]
        last_item = self.heap.pop()
        
        if not self.is_empty():
            self.heap[0] = last_item
            self.heapify_down(0)
        
        return min_item
    
    def peek_min(self):
        if self.is_empty():
            raise IndexError("Heap is empty.")
        
        return self.heap[0]
    
    def __len__(self):
        return len(self.heap)
