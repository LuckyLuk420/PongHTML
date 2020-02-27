from browser import window

gamejs = window.gamejs

class BinaryHeap():
    
    # score function must be javascript compatible (it runs in javascript context)
    def __init__(self, scoreFunction):
        self.heap = gamejs.math.binaryheap.BinaryHeap.new(scoreFunction)
    
    def pop(self):
        return self.heap.pop()
    
    def push(self, element):
        return self.heap.push(element)
    
    def remove(self, element):
        return self.heap.remove(element)
    
    def size(self):
        return self.heap.size()
