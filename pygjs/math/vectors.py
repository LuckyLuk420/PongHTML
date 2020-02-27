from browser import window

gamejs = window.gamejs

def add(a, b):
    return gamejs.math.vectors.add(a, b)

def angle(a, b):
    return gamejs.math.vectors.angle(a, b)

# variable number of arguments led me to this
centroid = gamejs.math.vectors.centroid

def distance(origin, target):
    return gamejs.math.vectors.distance(origin, target)

def divide(a, s):
    return gamejs.math.vectors.divide(a, s)

def dot(a, b):
    return gamejs.math.vectors.dot(a, b)

def multiply(a, b):
    return gamejs.math.vectors.multiply(a, b)

def rotate(vector, angle):
    return gamejs.math.vectors.rotate(vector, angle)

def subtract(a, b):
    return gamejs.math.vectors.subtract(a, b)

def truncate(v, maxlength):
    return gamejs.math.vectors.truncate(v, maxlength)

def unit(vector):
    return gamejs.math.vectors.unit(vector)
