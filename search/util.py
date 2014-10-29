'''
Created on Oct 26, 2014

@author: avinav
'''
import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
    def push(self,item,priority):
        pair = (priority, item)
        heapq.heappush(self.heap, pair)
    def pop(self):
        (priority, item) =  heapq.heappop(self.heap)
        return (item,priority)
    def isEmpty(self):
        return len(self.heap) == 0


class Queue:
    def __init__(self):
        self.list = []
    def push(self,item):
        self.list.append(item)
    def pop(self):
        return self.list.pop(0)
    def isEmpty(self):
        return len(self.list) == 0

class Stack:
    def __init__(self):
        self.list = []
    def push(self,item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()
    def isEmpty(self):
        return len(self.list) == 0


