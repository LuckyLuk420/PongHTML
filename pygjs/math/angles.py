from browser import window

gamejs = window.gamejs

def degrees(radians):
    return gamejs.math.angles.degrees(radians)

def normalizeDegrees(absolute):
    return gamejs.math.angles.normaliseDegrees(absolute)

def normalizeRadians(absolute):
    return gamejs.math.angles.normaliseRadians(absolute)

def radians(degrees):
    return gamejs.math.angles.radians(degrees)
