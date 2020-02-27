from browser import window

gamejs = window.gamejs

def make_relative(uri):
    return gamejs.utils.uri.makeRelative(uri)

def match(uri):
    return gamejs.utils.uri.match(uri)

def resolve(uri, path):
    return gamejs.utils.uri.resolve(uri, path)
