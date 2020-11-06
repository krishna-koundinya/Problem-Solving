# Source: Elements of Programming Interviews

# Problem: Optimum Assignment of Tasks (17. 1)
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)

def optimum_task_assignment(task_durations):
    
    task_durations.sort()
    
    tup = ('task1', 'task2')
    
    i = 0
    j = len(task_durations)-1
    
    paired_tasks = []
    
    while i < j:
        paired_tasks.append(((tup[0], task_durations[i]), \
        (tup[1], task_durations[j])))
        i += 1
        j -= 1
        
    if i == j:
        paired_tasks.append(((tup[0], task_durations[i]), \
        (tup[1], None)))
        
    return paired_tasks
    
print(optimum_task_assignment([5, 2, 1, 6, 4, 4]))