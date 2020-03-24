class PriorityQueue:
    def __init__(self, priority_function):
        self.queue = []
        self.func = priority_function
    
    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        return self.queue[0]

    def push(self, item):
        pos = 0
        found = False

        while(not found and pos < len(self.queue)):
            if(self.func(item, self.queue[pos])):
                found = True
            else:
                pos+=1
        
        self.queue.insert(pos, item)

    def pop(self):
        self.queue.pop(0)
