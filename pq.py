import heapq

a = [2 , 5 , 3, 8, 9, 6]

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0
        self.temp = {}

    def push(self, item, priority):

        values_list = list((self.temp).values())
        if item in values_list:
            return False

            
        self.temp[priority] = item
        heapq.heappush(self.heap, priority)
        self.count = self.count + 1
 #       return print(self.heap)

    def pop(self):
        self.count = self.count - 1
        return self.temp[heapq.heappop(self.heap)]
        

    def isEmpty(self):
        if self.count:
            return False
        else:
            return True      

    def update(self, item, priority):
        
        values_list = list((self.temp).values())
        if item not in values_list:
            self.temp[priority] = item
            heapq.heappush(self.heap, priority)
            self.count = self.count + 1
          #  return print(self.heap)

        else:
            prev_priority = values_list.index(item)
            if prev_priority < priority:
                return print("nothing changed")
            else:
                ind = self.heap.remove(prev_priority)
                heapq.heapify(self.heap)
                del self.temp[prev_priority]
                self.temp[priority] = item
                heapq.heappush(self.heap, priority)
        #        return print(self.heap)
                
                

pq = PriorityQueue()
pq.push('task0', 0)
print(pq.heap)
pq.push('task1', 1)
print(pq.heap)
pq.push('task2', 2)
print(pq.heap)
pq.push('task3', 3)
print(pq.heap)
min = pq.pop()
print(min)
print(pq.heap)

min = pq.pop()
print(min)
print(pq.heap)

min = pq.pop()
print(min)
print(pq.heap)