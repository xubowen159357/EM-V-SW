from data.code.pygamelocals import pygamelocals as pg
from data.code.jsonPy import jsonPy as jsonpy
from data.code.Loadcode import Loadcode as load
from tqdm.rich import tqdm,trange
import time
import sys
import os

class MAIN:
    def __init__(self) -> None:
        self.ADDONLIST=jsonpy.FrIn(jsonpy.load('data/addon/addon.json'))
        self.IMAGELIST=os.listdir('data/image')
        self.FONT=['data/addon/main/font/JETBRAINSMONO-LIGHT.TTF','data/addon/main/font/INKFREE.TTF','data/addon/main/font/SIMKAI.TTF']
        self.SETTING=jsonpy.FrIn(jsonpy.load('data/setting/setting.json'))
        self.LANG={}
        self.SOUNDS={}
        self.images=load.images.images()
        self.addon=load.addons.addons()
        self.loadself()

    def loadself(self) -> None:
        print(pg.colormode("Python version:\n",pg.gb),pg.colormode(sys.version,pg.r))
        for i in tqdm(list(self.ADDONLIST.dict.keys())):
            if self.ADDONLIST.dict[i]:self.addon.add(load.addons.Load(i, jsonpy))
        for i in tqdm(self.IMAGELIST):
            self.images.add(load.images.Load(i, jsonpy))
        #setting Load
        #lang part
        Lang=self.SETTING.dict.get('$Lang')
        Main_Lang=Lang[0]
        Appde_Lang=Lang[1]
        Langs=os.listdir(self.addon.addons['00000000-0000-0000-0000-000000000001'][0]+"/lang")
        Langs:list[str]
        langfile=None
        for i in tqdm(Langs):
            k=i.split("_")
            if k[0]!=Main_Lang:
                continue
            elif k[1]!=Appde_Lang:
                continue
            else:langfile=i
        if langfile==None:
            raise FileNotFoundError
        for i in tqdm(open(self.addon.addons['00000000-0000-0000-0000-000000000001'][0]+f"/lang/{langfile}",encoding='utf-8').readlines()):
            i=i.strip()
            k=i.split('=')
            self.LANG[k[0]]=k[1]
        for i in tqdm(open('data/sounds/sounds.ini',encoding='utf-8').readlines()):
            i=i.strip()
            k=i.split('=')
            self.SOUNDS[k[0]]=k[1]
