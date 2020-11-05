# Sources: Elements of Programming Interviews
# educative.io

# Alternative solution for merge-k-sorted-arrays

# Merging k sorted arrays using Min Heap
# Time Complexity: O(NKlog(K)), where N is the total number of 
# elements in array and K is the number of nested arrays
# Space Complexity: O(k) (extra space)



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
    
print(merge_sorted_arrays([[3, 5, 7], [0, 6], [0, 6, 28]]))