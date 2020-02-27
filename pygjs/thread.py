from browser import window

gamejs = window.gamejs

# wrapper for a very javascript based thing, returns javascript object, runs javascript file
# see gamejs/thread
def worker(workermodule):
    return gamejs.thread.Worker.new(workermodule)
