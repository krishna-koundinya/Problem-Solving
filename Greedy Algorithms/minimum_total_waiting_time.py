# Source Elements of Programming Interviews

# Problem: Schedule to Minimize Waiting Time (17.2)
# Given service times = [2, 5, 1, 3]
# Scheduling in that order gives:
# Wait time = 0 +(2) + (2+5) + (2+5+1) = 17
# Using minimum service time first we get
# Wait time = 0 + (1) +(1+2) + (1+2+3) = 10
# Time Complexity: O(nlog(n))
# Space Complexity: O(1)

def minimum_total_waiting_times(service_times):
    service_times.sort()
    total_waiting_time = 0
    for i in range(len(service_times)):
        num_remaining_queries = len(service_times) - (i+1)
        total_waiting_time += service_times[i] * num_remaining_queries
        
    return total_waiting_time
    
print(minimum_total_waiting_times([2, 5, 1, 3]))