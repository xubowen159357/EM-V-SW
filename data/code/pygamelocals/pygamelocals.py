from .colour import *


print('From %s.'%colormode('xu.bw',g,light))
print('NEAM:',colormode('DZJZG',r,light))
print(colormode('Loading..',b,shard))


from pygame.image import load
from .import windowAPI
from . import locals
from pygame import *
import pygame
import time
import threading

Clock=pygame.time.Clock()

class Time:
    def __init__(self,Update_speed) -> None:
        self.cick=60/(Update_speed+2)
        self.tick=0
        self.s=0
        self.thread={}
        self.update=threading.Thread(target=self.uptick)
        self.update.daemon=True
        self.update.start()
    def uptick(self):
        self.tick+=1
        if self.tick>=60:self.s+=1;self.tick=0
        time.sleep(self.cick)
    def addThread(self,name:str)->threading.Thread:
        self.thread[name]=threading.Thread

