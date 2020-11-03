# Source Elements of Programming for interviews

# Merging k sorted arrays using Min Heap
# Time Complexity: O(NKlog(K)), where N is the number of elements
# in array and K is the number of nested arrays
# Space Complexity: O(k) (extra space)

import heapq
def merge_sorted_arrays(arrays):
    min_heap = []
    sorted_array_iters = [iter(x) for x in arrays]
    
    for i, it in enumerate(sorted_array_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
            
    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_array_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
            
    return result
    
print(merge_sorted_arrays([[3, 5, 7], [0, 6], [0, 6, 28]]))