# Source Elements of Programming Interviews 10.2
# sort-k-increasing-decreasing-sequence
# Time Complexity: O(Nlog(K))
# Space Complexity: O(N)

# Min-Heap Implementation
class minHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)
        
    def getMin(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def removeMin(self):
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__minHeapify(0)
            return min
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None
    
    def __percolateUp(self, index):
        parent = (index-1)//2
        if index <= 0:
            return
        elif self.heap[parent] >= self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            self.__percolateUp(parent)
    
    def __minHeapify(self, index):
        left = (index*2)+1
        right = (index*2)+2
        largest = index
        if len(self.heap) > left and self.heap[largest] >= self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] >= self.heap[right]:
            largest = right
        
        if largest != index:
            temp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = temp
            self.__minHeapify(largest)
    
    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self.__minHeapify(i)

def adjust_arrays(arrays):
    maxi = max([len(element) for element in arrays])
    for i in arrays:
        n = len(i)
        if n < maxi:
            for j in range(n, maxi):
                i.append(None)
        else:
            pass
    return maxi, arrays
            
def merge_sorted_arrays(arrays):
    maxi, arrays = adjust_arrays(arrays)
    m = minHeap()
    res = []
    inner = 0
    while inner < 1:
        for outer in arrays:
            if outer[inner] is not None:
                m.insert(outer[inner])
        
        res.append(m.removeMin())
        inner += 1
    
    while inner < maxi and m.getMin() is not None:
        for outer in arrays:
            if outer[inner] is not None:
                m.insert(outer[inner])
                res.append(m.removeMin())
        
        inner += 1
    
    while m.getMin() is not None:
        res.append(m.removeMin())
        
    return res
    
def sort_k_increasing_decreasing_sequence(array):
    sorted_subarrays = []
    increasing, decreasing = range(2)
    subarray_type = increasing
    start_idx = 0
    
    for i in range(1, len(array)+1):
        if (i==len(array) or \
            (array[i-1] < array[i] and subarray_type==decreasing) or \
            (array[i-1] >= array[i] and subarray_type==increasing)):
            
            sorted_subarrays.append(array[start_idx:i] if subarray_type==increasing \
            else array[i-1:start_idx:-1])
            start_idx = i
            subarray_type = (decreasing if subarray_type==increasing else increasing)
            
    return merge_sorted_arrays(sorted_subarrays)
    
print(sort_k_increasing_decreasing_sequence([57, 131, 493, 294, 221, 339, 418, 452, 442, 190]))