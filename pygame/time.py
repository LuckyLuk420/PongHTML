from browser import window, timer
import pygame
from datetime import datetime

gamejs = window.gamejs

DELAYED = False

def get_ticks():
    dt = datetime.now() - pygame.start_time
    ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    return ms


def set_timer(eventid, ms):
    def fire():
        nonlocal eventid
        
        pygame.event.post(pygame.event.Event(eventid))
    
    if eventid not in set_timer.timers:
        set_timer.timers[eventid] = timer.set_interval(fire, ms)
    else:
        timer.clear_interval(set_timer.timers[eventid])
        if ms != 0:
            set_timer.timers[eventid] = timer.set_interval(fire, ms)
set_timer.timers = {}

# to grab the benefits the below code, use the eventloop augmentation in pygame.event
def wait(ms):
    global DELAYED
    
    DELAYED = True
    
    def undelay():
        global DELAYED
        
        DELAYED = False
    
    timer.set_timeout(undelay, ms)

def delay(ms):
    wait(ms)

class Clock():
    
    def __init__(self):
        self.framerate = 0
        self.lastcall = datetime.now()
        self.ms = 0
    
    def tick(self, framerate=0):
        self.framerate = framerate
        dt = datetime.now() - self.lastcall
        self.ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
        self.lascall = datetime.now()
        return self.ms
    
    def tick_busy_loop(self, framerate=0):
        self.tick(framerate)
    
    def get_time(self):
        return self.ms
    
    def get_rawtime(self):
        return self.ms
    
    def get_fps(self):
        pass

clock = Clock()
