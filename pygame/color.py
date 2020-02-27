from .colour import Color as Colour
import math

class InvalidArgumentError(Exception):
    pass

class Color():
    
    def __init__(self, r, g=None, b=None, a=None):
        if type(r) is str:
            if r[0] == '#':
                c = r[0:7]
                self.color = Colour()
                self.color.set_hex(c)
                a = r[-2:]
                a = int(a, 16)
                self.alpha = a / 255
            else:
                self.color = Colour(r)
                self.alpha = 1.0
            self.original = (self.r, self.g, self.b, self.a)
        else:
            self.color = Colour()
            self.color.red = (r / 255) if r else 0
            self.color.green = (g / 255) if g else 0
            self.color.blue = (b / 255) if b else 0
            self.alpha = (a / 255) if a else 1
            self.original = (r, g, b, a)
    
    def getColour(self):
        return self.color
    
    def getRGBA(self):
        return 'rgba(' + str(self.r) + ', ' + str(self.g) + ', ' + str(self.b) + ', ' + str(self.alpha) + ')';
    
    def get_r(self):
        return int(self.color.red * 255)
    
    def set_r(self, r):
        self.color.red = r / 255
    
    def get_g(self):
        return int(self.color.green * 255)
    
    def set_g(self, g):
        self.color.green = g / 255
    
    def get_b(self):
        return int(self.color.blue * 255)
    
    def set_b(self, b):
        self.color.blue = b / 255
    
    def get_a(self):
        return int(self.alpha * 255)
    
    def set_a(self, a):
        self.alpha = alpha
    
    def get_rgb(self):
        return (int(self.color.red * 255), int(self.color.green * 255), int(self.color.blue * 255))
    
    def set_rgb(self, rgb):
        for a in range(3):
            rgb[a] = rgb[a] / 255
        self.color.red = rgb[0]
        self.color.green = rgb[1]
        self.color.blue = rgb[2]
    
    # adapted from pygame/src/color.c [_color_get_cmy()]
    def get_cmy(self):
        return (1 - self.color.red, 1 - self.color.green, 1 - self.color.blue)
    
    # adapted from pygame/src/color.c [_color_set_cmy()]
    def set_cmy(self, cmy):
        for a in cmy:
            if a < 0 or a > 1:
                raise InvalidArgumentException("Color: Invalid Argument")   
        self.color.red = 1 - cmy[0]
        self.color.green = 1 - cmy[1]
        self.color.blue = 1 - cmy[2]
    
    # adapted from pygame/src/color.c [_color_get_hsva()]
    def get_hsva(self):    
        hsv = [0, 0, 0]
        frgb = [self.color.red, self.color.green, self.color.blue, self.alpha];
        maxv = max(frgb)
        minv = min(frgb)
        diff = maxv - minv
        
        hsv[2] = 100 * maxv
        
        if maxv == minv:
            hsv[0] = 0
            hsv[1] = 0
            return (hsv[0], hsv[1], hsv[2], frgb[3] *100)
        
        hsv[1] = 100 * (maxv - minv) / maxv
        
        if maxv == frgb[0]:
            hsv[0] = math.fmod((60 * ((frgb[1] - frgb[2]) / diff)), 360)
        elif maxv == frgb[1]:
            hsv[0] = (60 * ((frgb[2] - frgb[0]) / diff)) + 120
        else:
            hsv[0] = (60 * ((frgb[0] - frgb[1]) / diff)) + 240
        
        if hsv[0] < 0:
            hsv[0] += 360
        
        return (hsv[0], hsv[1], hsv[2], frgb[3] *100)
    
    # adapted from pygame/src/color.c [_color_set_hsva()]
    def set_hsva(self, hsva):
        if hsva[0] < 0 or hsva[0] > 360:
            raise InvalidArgumentError("Color: Invalid Argument")
        if hsva[1] < 0 or hsva[1] > 100:
            raise InvalidArgumentError("Color: Invalid Argument")
        if hsva[2] < 0 or hsva[2] > 100:
            raise InvalidArgumentError("Color: Invalid Argument")
        if hsva[3] < 0 or hsva[3] > 100:
            raise InvalidArgumentError("Color: Invalid Argument")
        
        self.alpha = hsva[3] / 100
        
        s = hsva[1] / 100
        v = hsva[2] / 100
        
        hi = int(math.floor(hsva[0] / 60))
        f = (hsva[0] / 60) - hi
        p = v * (1 - s)
        q = v * (1 - s * f)
        t = v * (1 - s * (1 - f))
        
        if hi == 1:
            self.color.red = q
            self.color.green = v
            self.color.blue = p
        elif hi == 2:
            self.color.red = p
            self.color.green = v
            self.color.blue = t
        elif hi == 3:
            self.color.red = p
            self.color.green = q
            self.color.blue = v
        elif hi == 4:
            self.color.red = t
            self.color.green = p
            self.color.blue = v
        elif hi == 5:
            self.color.red = v
            self.color.green = p
            self.color.blue = q
        else:
            self.color.red = v
            self.color.green = t
            self.color.blue = p
    
    # adapted from pygame/src/color.c [_color_get_hsla()]
    def get_hsla(self):
        hsl = [0, 0, 0]
        frgb = [self.color.red, self.color.green, self.color.blue, self.alpha];
        
        maxv = max(frgb)
        minv = min(frgb)
        diff = maxv - minv
        
        hsl[2] = 50 * (maxv + minv)
        
        if maxv == minv:
            hsl[1] = 0
            hsl[0] = 0
            return (hsl[0], hsl[1], hsl[2], frgb[3] * 100)
        
        if hsl[2] <= 50:
            hsl[1] = diff / (maxv + minv)
        else:
            hsl[1] = diff / (2 - maxv - minv)
        hsl[1] *= 100
        
        if maxv == frgb[0]:
            hsl[0] = math.fmod((60 * ((frgb[1] - frgb[2]) / diff)), 360)
        elif maxv == frgb[1]:
            hsl[0] = (60 * ((frgb[2] - frgb[0]) / diff)) + 120
        else:
            hsl[0] = (60 * ((frgb[0] - frgb[1]) / diff)) + 240
        
        if hsl[0] < 0:
            hsl[0] += 360
        
        return (hsl[0], hsl[1], hsl[2], frgb[3] * 100)
    
    # adapted from pygame/src/color.c [_color_set_hsla()]
    def set_hsla(self, hsla):
        if hsla[0] < 0 or hsla[0] > 360:
            raise InvalidArgumentError("Color: Invalid Argument")
        if hsla[1] < 0 or hsla[1] > 100:
            raise InvalidArgumentError("Color: Invalid Argument")
        if hsla[2] < 0 or hsla[2] > 100:
            raise InvalidArgumentError("Color: Invalid Argument")
        if hsla[3] < 0 or hsla[3] > 100:
            raise InvalidArgumentError("Color: Invalid Argument")
        
        self.alpha = hsla[3] / 100
        
        s = hsla[1] / 100
        l = hsla[2] / 100
        
        if s == 0:
            self.color.red = l
            self.color.green = l
            self.color.blue = l
            return
        
        q = float(0.0)
        if l < 0.5:
            q = l * (1 + s)
        else:
            q = l + s - (l * s)
        p = 2 * l - q
        
        ht = hsla[0] / 360
        
        h = ht + (1/3)
        if h < 0:
            h += 1
        elif h > 1:
            h -= 1
        
        if h < (1/6):
            self.color.red = p + ((q - p) * 6 * h)
        elif h < 0.5:
            self.color.red = q
        elif h < (2/3):
            self.color.red = p + ((q - p) * 6 * ((2/3) - h))
        else:
            self.color.red = p
        
        h = ht
        if h < 0:
            h += 1
        elif h > 1:
            h -= 1
        
        if h < (1/6):
            self.color.green = p + ((q - p) * 6 * h)
        elif h < 0.5:
            self.color.green = q
        elif h < (2/3):
            self.color.green = p + ((q - p) * 6 * ((2/3) - h))
        else:
            self.color.green = p
        
        h = ht - (1/3)
        if h < 0:
            h += 1
        elif h > 1:
            h -= 1
        
        if h < (1/6):
            self.color.blue = p + ((q - p) * 6 * h)
        elif h < 0.5:
            self.color.blue = q
        elif h < (2/3):
            self.color.blue = p + ((q - p) * 6 * ((2/3) - h))
        else:
            self.color.blue = p
    
    # adapted from pygame/src/color.c [_color_get_i1i2i3()]
    def get_i1i2i3(self):
        frgb = [self.color.red, self.color.green, self.color.blue, self.alpha];
        
        return ((frgb[0] + frgb[1] + frgb[2]) / 3,
                (frgb[0] - frgb[2]) / 2,
                (2 * frgb[1] - frgb[0] - frgb[2]) / 4)
    
    # adapted from pygame/src/color.c [_color_set_i1i2i3()]
    def set_i1i2i3(self, i1i2i3):
        if i1i2i3[0] < 0 or i1i2i3[1] > 1:
            raise InvalidArgumentError("Color: Invalid Argument")
        if i1i2i3[1] < -0.5 or i1i2i3[1] > 0.5:
            raise InvalidArgumentError("Color: Invalid Argument")
        if i1i2i3[2] < -0.5 or i1i2i3[2] > 0.5:
            raise InvalidArgumentError("Color: Invalid Argument")
        
        ab = i1i2i3[0] - i1i2i3[1] - 2 * i1i2i3[2] / 3
        ar = 2 * i1i2i3[1] + ab
        ag = 3 * i1i2i3[0] - ar - ab
        
        self.color.red = ar
        self.color.green = ag
        self.color.blue = ab
    
    r = property(get_r, set_r)
    g = property(get_g, set_g)
    b = property(get_b, set_b)
    a = property(get_a, set_a)
    rgb = property(get_rgb, set_rgb)
    cmy = property(get_cmy, set_cmy)
    hsva = property(get_hsva, set_hsva)
    hsla = property(get_hsla, set_hsla)
    i1i2i3 = property(get_i1i2i3, set_i1i2i3)
    
    def normalize(self):
        return (self.color.red, self.color.green, self.color.blue, self.alpha)
    
    # adapted from pygame/src/color.c [_color_correct_gamma()]
    def correct_gamma(gamma):
        frgba = [math.pow(self.color.red, gamma), math.pow(self.color.green, gamma),
                 math.pow(self.color.blue, gamma), math.pow(self.alpha, gamma)]
        rgba = [0, 0, 0, 0]
        for a in range(4):
            rgba[a] = 255 if frgba[a] > 1 else (0 if frgba[a] < 0 else (frgba[a] * 255 + .5))
        
        return tuple(rbga)
    
    # adapted from pygame/src/color.c [_color_add()]
    def __add__(self, color):
        assert isinstance(color, Color)
        ret = Color()
        ret.color.red = min(self.color.red + color.color.red, 1)
        ret.color.green = min(self.color.green + color.color.green, 1)
        ret.color.blue = min(self.color.blue + color.color.blue, 1)
        ret.alpha = min(self.alpha + color.alpha, 1)
    
    # adapted from pygame/src/color.c [_color_sub()]
    def __sub__(self, color):
        assert isinstance(color, Color)
        ret = Color()
        ret.color.red = max(self.color.red - color.color.red, 0)
        ret.color.green = max(self.color.green - color.color.green, 0)
        ret.color.blue = max(self.color.blue - color.color.blue, 0)
        ret.alpha = max(self.alpha - color.alpha, 0)
    
    # adapted from pygame/src/color.c  [_color_mul()]
    def __mul__(self, color):
        assert isinstance(color, Color)
        ret = [min(self.r * color.r, 255), min(self.g * color.g, 255),
               min(self.b * color.b, 255), min(self.a * color.a, 255)]
        return Color(ret[0], ret[1], ret[2], ret[3])
    
    # adapted from pygame/src/color.c [_color_div()]
    def __div__(self, color):
        assert isinstance(color, Color)
        ret = [0, 0, 0, 0]
        if color.r != 0:
            ret[0] = self.r / color.r
        if color.g != 0:
            ret[1] = self.g / color.g
        if color.b != 0:
            ret[2] = self.b / color.b
        if color.a != 0:
            ret[3] = self.a / color.a
        return Color(ret[0], ret[1], ret[2], ret[3])
    
    # adapted from pygame/src/color.c [_color_mod()]
    def __mod__(self, color):
        assert isinstance(color, Color)
        ret = [0, 0, 0, 0]
        if color.r != 0:
            ret[0] = self.r % color.r
        if color.g != 0:
            ret[1] = self.g % color.g
        if color.b != 0:
            ret[2] = self.b % color.b
        if color.a != 0:
            ret[3] = self.a % color.a
    
    # adapted from pygame/src/color.c [_color_inv()]
    def __invert__(self):
        return Color(255 - color.r, 255 - color.g, 255 - color.b, 255 - color.a)
    
    def __cmp__(self, other):
        assert isinstance(other, Color)
        return cmp((self.r, self.g, self.b, self.a),
                   (other.r, other.g, other.b, other.a));
    