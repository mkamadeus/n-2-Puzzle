from puzzle import Puzzle
from priorityqueue import PriorityQueue

a = Puzzle("./input/1.txt")

a.output_board()

print("Solveable:", a.is_solveable())
if(a.is_solveable()):
    a.solve()
# pq = PriorityQueue(lambda x,y : x<y)

# pq.push(98)
# pq.push(3)
# pq.push(1)
# pq.push(5)
# pq.push(999)

# print(pq.queue)