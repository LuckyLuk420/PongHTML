from browser import window

gamejs = window.gamejs

def decode(uinput):
    return gamejs.utils.base64.decode(uinput)

def decode_as_array(uinput, ubytes=1):
    return gamejs.utils.base64.decodeAsArray(uinput, ubytes)
