from browser import window

gamejs = window.gamejs

# returns a javascript XMLHttpRequest object
def ajax(method, url, data, utype):
    return gamejs.http.ajax(method, url, data, utype)

# returns a javascript XMLHttpRequest object
def get(url):
    return gamejs.http.get(url)

# returns a javascript XMLHttpRequest Object
def post(url, data, utype):
    return gamejs.http.post(url, data, utype)

# returns javascript objects (see gamejs.http.stringify)
def load(url):
    return gamejs.http.load(url)

# returns javascript objects (see gamejs.http.strinigy)
def save(url, data, utype):
    return gamejs.http.save(url, data, utype)
