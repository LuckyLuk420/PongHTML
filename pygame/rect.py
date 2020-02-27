from browser import window

gamejs = window.gamejs

class Rect():
    
    def __init__(self, left=0, top=0, width=0, height=0, obj=None):
        if obj == None:
            if type(left) is tuple or type(left) is list:
                if type(top) is tuple or type(top) is list:
                    self.rect = gamejs.Rect.new(left, top)
                else:
                    self.rect = gamejs.Rect.new(left)
            else:
                self.rect = gamejs.Rect.new(left, top, width, height);
        else:
            self.rect = gamejs.Rect.new(obj)
    
    def get_x(self):
        return self.rect.x
    
    def set_x(self, x):
        self.rect.x = x
        
    def get_y(self):
        return self.rect.y
    
    def set_y(self, y):
        self.rect.x = y
    
    def get_top(self):
        return self.rect.top
    
    def set_top(self, top):
        self.rect.top = top
    
    def get_left(self):
        return self.rect.left
    
    def set_left(self, left):
        self.rect.left = left
    
    def get_bottom(self):
        return self.rect.bottom
    
    def set_bottom(self, bottom):
        self.rect.bottom = bottom
    
    def get_right(self):
        return self.rect.right
    
    def set_right(self):
        self.rect.right = right
    
    def get_topleft(self):
        return self.rect.topleft
    
    def set_topleft(self, topleft):
        self.rect.topleft = topleft
    
    def get_bottomleft(self):
        return self.rect.bottomleft
    
    def set_bottomleft(self, bottomleft):
        self.rect.bottomleft = bottomleft
    
    def get_topright(self):
        return self.rect.topright
    
    def set_topright(self, topright):
        self.rect.topright = topright
    
    def get_bottomright(self):
        return self.rect.bottomright
    
    def set_bottomright(self, bottomright):
        self.rect.bottomright = bottomright
    
    def get_midtop(self):
        dist = (self.rect.right - self.rect.left) / 2
        return (self.rect.left + dist, self.rect.top)
    
    def set_midtop(self, coordsx, coordsy=0):
        if type(coordsx) is tuple or type(coordsx) is list:
            coordsy = coordsx[1]
            coordsx = coordsx[0]
        dist = (self.rect.right - self.rect.left) / 2
        self.rect.left = coordsx - dist
        self.rect.top = coordsy
    
    def get_midleft(self):
        dist = (self.rect.bottom - self.rect.top) / 2
        return (self.rect.left, self.rect.top + dist)
    
    def set_midleft(self, coordsx, coordsy=0):
        if type(coordsx) is tuple or type(coordsx) is list:
            coordsy = coordsx[1]
            coordsx = coordsx[0]
        dist = (self.rect.bottom - self.rect.top) / 2
        self.rect.left = coordsx
        self.rect.top = coordsy - dist
    
    def get_midbottom(self):
        dist = (self.rect.right - self.rect.left) / 2
        return (self.rect.left + dist, self.rect.bottom)
    
    def set_midbottom(self, coordsx, coordsy=0):
        if type(coordsx) is tuple or type(coordsx) is list:
            coordsy = coordsx[1]
            coordsx = coordsx[0]
        dist = (self.rect.right - self.rect.left) / 2
        self.rect.left = coordsx - dist
        self.rect.bottom = coordsy
    
    def get_midright(self):
        dist = (self.rect.bottom - self.rect.bottom) / 2
        return (self.rect.right, self.rect.top + dist)
    
    def set_midright(self, coordsx, coordsy=0):
        if type(coordsx) is tuple or type(coordsx) is list:
            coordsy = coordsx[1]
            coordsx = coordsx[0]
        dist = (self.rect.bottom - self.rect.top) / 2
        self.rect.right = coordsx
        self.rect.top = coordsy - dist
    
    def get_center(self):
        return self.rect.center
    
    def set_center(self, center):
        self.rect.center = center
    
    def get_centerx(self):
        return self.rect.center[0]
    
    def set_centerx(self, centerx):
        center = self.rect.center
        center[0] = centerx
        self.rect.center = center
    
    def get_centery(self):
        return self.rect.center[1]
    
    def set_centery(self, centery):
        center = self.rect.center
        center[1] = centery
        self.rect.center = center
    
    def get_size(self):
        return (self.rect.width, self.rect.height)
    
    def set_size(self, size):
        self.rect.width = size[0]
        self.rect.height = size[1]
    
    def get_width(self):
        return self.rect.width
    
    def set_width(self, width):
        self.rect.width = width
    
    def get_height(self):
        return self.rect.height
    
    def set_height(self, height):
        self.rect.height = height
    
    def get_w(self):
        return self.rect.width
    
    def set_w(self, w):
        self.rect.width = w
    
    def get_h(self):
        return self.rect.height
    
    def set_h(self, h):
        self.rect.height = h
    
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    top = property(get_top, set_top)
    left = property(get_left, set_left)
    bottom = property(get_bottom, set_bottom)
    right = property(get_right, set_right)
    topleft = property(get_topleft, set_topleft)
    bottomleft = property(get_bottomleft, set_bottomleft)
    topright = property(get_topright, set_topright)
    bottomright = property(get_bottomright, set_bottomright)
    midtop = property(get_midtop, set_midtop)
    midleft = property(get_midleft, set_midleft)
    midbottom = property(get_midbottom, set_midbottom)
    midright = property(get_midright, set_midright)
    center = property(get_center, set_center)
    centerx = property(get_centerx, set_centerx)
    centery = property(get_centery, set_centery)
    size = property(get_size, set_size)
    width = property(get_width, set_width)
    height = property(get_height, set_height)
    w = property(get_w, set_w)
    h = property(get_h, set_h)
    
    def copy(self):
        return Rect(obj=self.rect.clone())
    
    def move(self, x, y):
        return Rect(obj=self.rect.move(x, y))
    
    def move_ip(self, x, y):
        self.rect.moveIp(x, y)
    
    def inflate(self, x, y):
        return Rect(obj=self.rect.inflate(x, y))
    
    def inflate_ip(self, x, y):
        self.rect.inflateIp(x, y)
    
    def clamp(self, rect):
        return Rect(obj=gamejs.rect.clamp(rect.rect))
    
    def clamp_ip(self, rect):
        self.rect.clampIp(rect.rect)
    
    def clip(self, rect):
        return Rect(obj=self.rect.clip(rect.rect))
    
    def union(self, rect):
        return Rect(obj=self.rect.union(rect.rect))
    
    def union_ip(self, rect):
        self.rect = self.rect.union(rect.rect)
    
    def fit(self, rect):
        return Rect(obj=gamejs.rect.fit(rect.rect))
    
    def normalize(self):
        self.rect.normalize()
    
    def contains(self, rect):
        return self.rect.contains(rect.rect)
    
    def collidepoint(self, x, y=0):
        if type(x) is tuple or type(x) is list:
            y = x[1]
            x = x[0]
        return self.rect.collidePoint(x,y)
    
    def colliderect(self, rect):
        return self.rect.collideRect(rect.rect)
    
    def collidelist(self, rects):
        for a in range(len(rects)):
            if self.colliderect(rects[a]):
                return a
        return -1
    
    def collidelistall(self, rects):
        ret = []
        for a in range(len(rects)):
            if self.colliderect(rects[a]):
                ret.append(a)
        return ret
    
    def collidedict(self, rects):
        for key, val in rects.iteritems():
            if self.colliderect(val):
                return (key, val)
    
    def collidedictall(self, rects):
        ret = {}
        for key, val in rects.iteritems():
            if self.colliderect(val):
                ret[key] = val
        return ret
