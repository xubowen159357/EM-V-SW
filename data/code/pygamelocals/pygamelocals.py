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
    def __init__(self,Update_speed:int) -> None:
        self.cick=60/(Update_speed)
        self.tick=0
        self.s=0
        self.thread={}
        self.update=threading.Thread(target=self.uptick)
        self.update.daemon=True
        self.update.start()
    def uptick(self):
        while True:
            self.tick+=1
            if self.tick>=60:self.s+=1;self.tick=0
            time.sleep(self.cick/100)
    def addThread(self,name:str,cycle:int)->threading.Thread:
        self.thread[name]=self.ThreadTime(self.cick,cycle)
    def ThreadTime(self,cick:int,cycle:int=0):
        class TT:
            def __init__(Tt) -> None:
                Tt.time=0
                Tt.tick=0
                Tt.cick=cick
                Tt.cycle=cycle
                Tt.update=threading.Thread(target=Tt.uptick)
                Tt.update.daemon=True
                Tt.update.start()
            def uptick(Tt):
                while True:
                    Tt.tick+=1
                    if Tt.tick>=60:Tt.time+=1;Tt.tick=0
                    if Tt.cycle:
                        if Tt.time>Tt.cycle:Tt.time=0
                    time.sleep(Tt.cick/100)
        return TT()

class CLASSIOREDER:
    def __init__(self) -> None:
        self.IO={}
    def add(self,name:str,Object):
        self.IO[name]=Object
