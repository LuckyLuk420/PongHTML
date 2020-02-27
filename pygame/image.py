from browser import window

gamejs = window.gamejs

class UnsupportedFileType(Exception):
    pass

class UnsupportedFormat(Exception):
    pass

class UnsupportedFunction(Exception):
    pass

# to load an image you must preload it first, you MUST supply filename, not file object
def load(filename, namehint=""):
    return Surface(dimensions=(0,0), fromSurface=gamejs.image.load(filename))

# does not default to TGA, defaults to PNG
def save(surface, filename):
    ext = filename.split(".")
    if len(ext) > 1:
        ext = ext[len(ext)-1].lower()
    canvas = surface.surface.canvas
    url = ""
    if ext == "jpg" or ext == "jpeg":
        url = canvas.toDataURL("image/jpeg")
    elif ext == "png":
        url = canvas.toDataURL("image/png")
    elif ext == "gif":
        url = canvas.toDataURL("image/gif")
    elif ext == "bmp":
        url = canvas.toDataURL("image/bmp")
    elif ext == "tiff":
        url = canvas.toDataURL("image/tiff")
    else:
        raise UnsupportedFileType("image.save: unsupported file format")
    
    if hasattr(window, 'nw'):
        import re
        # we're in nw.js, prsumably
        fs = window.require("fs")
        data = re.sub(r"^data:image\/\w+;base64,", "", url)
        buf = window.Buffer.new(data, "base64")
        fs.writeFile(filename, buf)
    else:
        import re
        data = re.sub(r"^data:image\/\w+;", "data:application/octet-stream;", url)
        console.log(data)
        window.location.href = data

def get_extended():
    return True

# this is a wrapper to canvas imageData, RGBA is supported only, and flipped is not
def tostring(surface, format="RGBA", flipped=False):
    if format == "RGBA":
        array = gamejs.graphics.SurfaceArray.new(surface.surface)
        return array.imageData.data
    else:
        raise UnsupportedFormat("image.tostring: unsupported format")

# same as above
def fromstring(string, size, format="RGBA", flipped=False):
    if format == "RGBA":
        surface = Surface(dimensions=size)
        array = gamejs.graphics.SurfaceArray.new(surface.surface, string)
        surface = Surface(dimensions=size, fromSurface=array.makeSurface(array.buf32))
        return surface
    else:
        raise UnsupportedFormat("image.tostring: unsupported format")

# not supported
def frombuffer(string, size, format="RGBA"):
    raise UnsupportedFunction("image.frombuffer: unsupported function")
