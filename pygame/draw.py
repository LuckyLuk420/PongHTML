from browser import window
from .rect import Rect
import math

gamejs = window.gamejs

# not currently supported: returning affected pixel rectangles

def rect(surface, color, drect, width=0):
    gamejs.graphics.rect(surface.surface, color.getRGBA(), drect.rect, width)
    return Rect()

def polygon(surface, color, pointlist, width=0):
    gamejs.graphics.polygon(surface.surface, color.getRGBA(), pointlist, width)
    return Rect()

def circle(surface, color, pos, radius, width=0):
    gamejs.graphics.circle(surface.surface, color.getRGBA(), pos, radius, width)
    return Rect()

def ellipse(surface, color, rect, width=0):
    ctx = surface.surface.context
    ctx.save()
    ctx.beginPath()
    ctx.fillStyle = color.getRGBA()
    ctx.ellipse(rect.centerx, rect.centery, rect.width, rect.height, 0, 0, 2 * math.PI)
    if width:
        ctx.lineWidth = width
        ctx.stroke()
    else:
        ctx.fill()
    ctx.restore()
    return Rect()

def ellipse(surface, color, rect, start_angle, stop_angle, width=1):
    ctx = surface.surface.context
    ctx.save()
    ctx.beginPath()
    ctx.fillStyle = color.getRGBA()
    ctx.ellipse(rect.centerx, rect.centery, rect.width, rect.height, start_angle, stop_angle, 2 * math.PI)
    ctx.lineWidth = width
    ctx.stroke()
    ctx.restore()
    return Rect()

def line(surface, color, star_pos, end_pos, width=1):
    gamejs.graphics.line(surface.surface, color.getRGBA(), star_pos, end_pos, width)
    return Rect()

def lines(surface, color, closed, pointlist, width=1):
    gamejs.graphics.lines(surface.surface, color.getRGBA(), pointlist, width)
    return Rect()

# special anti-aliasing is not supported right now
def aaline(surface, color, startpos, endpos, blend=1):
    return line(surface, color, startpos, endpos)

def aalines(surface, color, closed, pointlist, blend=1):
    return lines(surface, color, closed, pointlist)
