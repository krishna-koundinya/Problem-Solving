# Source Elements of Programming Interviws 18.2
# William Fiset's Graph Theory playlist

# Paint a Boolean Matrix
# Flips the color of a cell and all its adjacent cells
# adjacent -> above, below, left, and right
# Time Complexity: O(Rows * Columns) for BFS
# Considering the fact that no.of vertices = rows*cols
# And no.of edges = 4*rows*cols
# Space Complexity: O(Rows * Columns)

from collections import deque
class ColorFill:
    def __init__(self, matrix, start):
        self.matrix = matrix
        self.R = len(matrix)
        self.C = len(matrix[0])
        self.color = abs(1-matrix[start[0]][start[1]])
        self.sr = start[0]
        self.sc = start[1]
        self.move_count = 0
        
        self.nodes_left_in_this_level = 1
        self.nodes_in_next_level = 0
        self.rq = deque()
        self.cq = deque()
        
        self.rv = [-1, 1, 0, 0]
        self.cv = [0, 0, -1, 1]
        
    def solve(self):
        self.rq.append(self.sr)
        self.cq.append(self.sc)
        
        while len(self.rq) > 0:
            r = self.rq.popleft()
            c = self.cq.popleft()
            
            self.matrix[r][c] = self.color
            self.explore_neighbors(r, c)
            self.nodes_left_in_this_level -= 1
            
            if self.nodes_left_in_this_level == 0:
                self.nodes_left_in_this_level = \
                self.nodes_in_next_level
                self.nodes_in_next_level = 0
                self.move_count += 1
        
        return self.matrix
            
    def explore_neighbors(self, r, c):
        for i in range(4):
            rr = r+self.rv[i]
            cc = c+self.cv[i]
            
            if rr < 0 or cc < 0:
                continue
            if rr >= self.R or cc >= self.C:
                continue
            if self.matrix[rr][cc] == self.color:
                continue
            
            self.matrix[rr][cc] = self.color
            self.rq.append(rr)
            self.cq.append(cc)
            self.nodes_in_next_level += 1
        
matrix = [[0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
          [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
          [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
          [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
          [1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
          [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]]

c1 = ColorFill(matrix, [5, 4])
m1 = c1.solve()
print(m1)
print("\n")
c2 = ColorFill(m1, [3, 6])
m2 = c2.solve()
print(m2)
