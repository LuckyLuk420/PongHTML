from browser import window

gamejs = window.gamejs

class UnimplementedMethod(Exception):
    pass

# this class is meant as an interface to inherit from, see gamejs/pathfinding
class Map():
    
    def actualDistance(self, pointa, pointb):
        raise UnimplementedMethod("pygjs.map.actualDistance: unimplemented method")
    
    def adjacent(self, origin):
        raise UnimplementedMethod("pygjs.map.adjacent: unimplemented method")
    
    def equals(self, a, b):
        raise UnimplementedMethod("pygjs.map.equals: unimplemented method")
    
    def estimatedDistance(self, pointa, pointb):
        raise UnimplementedMethod("pygjs.map.estimatedDistance: unimplemented method")
    
    def hash(self, a):
        raise UnimplementedMethod("pygjs.map.hash: unimplemented method")

# currently only accepts a javascript object as umap, NOT python (see gamjs/pathfinding)
def findRoute(umap, origin, destination, timeout):
    return gamejs.pathfinding.findRoute(umap, origin, destination, timeout)
