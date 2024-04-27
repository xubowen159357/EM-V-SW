from data.code.pygamelocals import pygamelocals as pg
from data.code.jsonPy import jsonPy as jsonpy
from data.code.Loadcode import Loadcode as load
from tqdm.rich import tqdm,trange
import os.path
import time
import sys
import os

class MAIN:
    def __init__(self) -> None:
        self.init()
        self.chcek()
        self.loadself()
        self.THREADS = {}
        if self.SETTING.dict.get('$Sound')['init']:
            pg.mixer.init()
            for i in range(2, 7):
                self.THREADS['thread'+str(i)] = pg.mixer.Channel(i)
        else:self.THREADS='disabled'

    def chcek(self) -> None:
        listofad=os.listdir('data/addon')
        del listofad[listofad.index('addon.json')]
        if len(listofad)!=len(self.ADDONLIST.dict.keys()):
            for i in listofad:
                self.ADDONLIST.dict[i]=1
        open('data/addon/addon.json','w',encoding='utf-8').write(jsonpy.To(self.ADDONLIST.dict).json)
        self.init()

    def init(self) -> None:
        self.ADDONLIST=jsonpy.FrIn(jsonpy.load('data/addon/addon.json'))
        self.IMAGELIST=os.listdir('data/image')
        self.FONT=['data/addon/main/font/JETBRAINSMONO-LIGHT.TTF','data/addon/main/font/INKFREE.TTF','data/addon/main/font/SIMKAI.TTF']
        self.SETTING=jsonpy.FrIn(jsonpy.load('data/setting/setting.json'))
        self.LANG={}
        self.SOUNDS={}
        self.images=load.images.images()
        self.addon=load.addons.addons()

    def loadself(self) -> None:
        print(pg.colormode("Python version:\n",pg.gb),pg.colormode(sys.version,pg.r))
        try:
            for i in tqdm(list(self.ADDONLIST.dict.keys())):
                if self.ADDONLIST.dict[i]:self.addon.add(load.addons.Load(i, jsonpy))
        except:
            a=open('data/addon/addon.json','w',encoding='utf-8')
            a.write('{}')
            a.close()
            self.init()
            self.chcek()
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

class USER:
    def __init__(self,ACCESS:MAIN) -> None:
        self.username=ACCESS.SETTING.dict.get('User')
        if not os.path.exists(f'data/setting/user/{self.username}.access.data'):
            if pg.windowAPI.mess.askyesno('ADD USER','Do you want to add user?'):open(f'data/setting/user/{self.username}.access.data','w',encoding='utf-8').write(r'{"maxscore":0,"developers":0}')
            else:os.startfile('data/setting/setting.json');pg.windowAPI.mess.showinfo('CONT ADD NEW USER','Please try others user.');sys.exit()
        self.user=jsonpy.FrIn(jsonpy.load(f'data/setting/user/{self.username}.access.data'))
        self.maxscore=self.user.dict.get('maxscore')
    def save(self):
        self.user.dict['maxscore']=self.maxscore
        open(f'data/setting/user/{self.user.dict.get("User")}.access.data','w',encoding='utf-8').write(jsonpy.To(self.user.dict).json)