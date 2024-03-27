from data.code.pygamelocals import pygamelocals as pg
from data.code.jsonPy import jsonPy as jsonpy
from data.code.uuidPy import uuidPy as uuidpy
from typing import Tuple, Union
import threading
import zipfile
import laoders
import random
import time
import math
import wget
import os


LAODER = laoders.MAIN()
RUN = 1
WID, HEI = 192*5, 108*5
UUID = uuidpy.uuidkey()
FPS = LAODER.SETTING.dict['FPS_MAX']
REBOOL = 10
ICON = 'data/setting/icon.ico'
ERROR = None
THREADS = {}
CAT=''

root = pg.windowAPI.Tk()
root.title(LAODER.LANG['Text.smellcaptain'])
root.wm_withdraw()
FULLSUCSSE = {'full': 0, 'max_size': root.wm_maxsize(), 'size': [WID, HEI]}
FULLSUCSSE['pos']=int((FULLSUCSSE['max_size'][0]+FULLSUCSSE['max_size'][1])/(WID+HEI))
pg.init()
ROOT = pg.display.set_mode([WID, HEI])
pg.display.set_caption(LAODER.LANG['Text.captain'])
pg.display.set_icon(pg.load(ICON))
pg.mouse.set_visible(False)
loop = 'screen'
time_killer = {'tick': 0, 'time': 0, 'clock1': 0}
# imang
temp = LAODER.images.images['7PHKQHQ0-CB90-QYL0-343S-3RRJYKDS1J1Q']
Schach = 0


for i in range(2, 7):
    THREADS['thread'+str(i)] = pg.mixer.Channel(i)


if LAODER.SETTING.dict['$version']['type'] == 'alpha' or LAODER.SETTING.dict['$version']['type'] == 'bate':
    if LAODER.LANG['Lang.type'] != 'zh':
        if not pg.windowAPI.mess.askretrycancel(f"Version {LAODER.SETTING.dict['$version']['type']}', f'You are currently using version {LAODER.SETTING.dict['$version']['type']}, this version usually has a lot of bugs, if you encounter, please do not tell me, because I am busy. Thank you for your cooperation!"):
            quit()
    else:
        if not pg.windowAPI.mess.askretrycancel(LAODER.SETTING.dict['$version']['type']+' 版本', f'你现在使用的是 {LAODER.SETTING.dict["$version"]["type"]} 版本, 此版本通常有很多Bug, 如果你遇到了, 请不要告诉我, 因为我很忙。谢谢合作！'):
            quit()


'''
surfacelook=pg.load(temp[0]+'/'+temp[1]['log'])
surfacelook=transform.scale(surfacelook,(WID,HEI))'''

# funanch of show


class API_8w52764y:
    def __init__(self) -> None:
        self.root = ROOT

    def blit(self, sur: pg.surface, rect: pg.rect.Rect, size: tuple = None, textrcet: pg.rect.Rect = False, movetext: list = None):
        if size != None and FULLSUCSSE['full'] and textrcet == False:
            size = [size[0]*FULLSUCSSE['pos'], size[1]*FULLSUCSSE['pos']]
            sur = pg.transform.scale(sur, size)
        elif size != None and textrcet == False:
            size = [size[0], size[1]]
            sur = pg.transform.scale(sur, size)
        elif textrcet != False:
            if FULLSUCSSE['full']:
                sur = pg.transform.scale(sur, (textrcet.w*FULLSUCSSE['pos'], textrcet.h*FULLSUCSSE['pos']))
                if movetext != None and type(movetext) != list:
                    if (type(rect) == list or type(rect) == tuple) and (rect[0]-textrcet.w & rect[1]-textrcet.h >= 0):
                        rect[0] -= textrcet.w
                        rect[1] -= textrcet.h
                    elif rect.x-textrcet.w >= 0 & rect.y-textrcet.h >= 0:
                        rect.x -= textrcet.w
                        rect.y -= textrcet.h
                elif movetext != None:
                    if type(rect) == list or type(rect) == tuple:
                        rect[0] -= movetext[0]
                        rect[1] -= movetext[1]
                    else:
                        rect.x -= movetext[0]
                        rect.y -= movetext[1]
        self.root.blit(sur, rect)
        return size

    def showtext(self, text: str, size: int, color: tuple = (0, 0, 0), font: str = None, bgcolor: Union[tuple, None] = None, antialias: int = 0, culertext=0):
        if culertext:
            if LAODER.LANG['Lang.type'] == 'zh':
                if font == None:
                    font = LAODER.FONT[2]
                return pg.font.Font(font, size).render(text, antialias, color, bgcolor)
            else:
                if font == None:
                    font = LAODER.FONT[0]
                return pg.font.Font(font, size).render(text, antialias, color, bgcolor)
        else:
            enl = ['Text.smellcaptain']
            if LAODER.LANG['Lang.type'] == 'zh' and not text in enl:
                if font == None:
                    font = LAODER.FONT[2]
                return pg.font.Font(font, size).render(LAODER.LANG[text], antialias, color, bgcolor)
            elif text in enl:
                return pg.font.Font(LAODER.FONT[1], size).render(LAODER.LANG[text], antialias, color, bgcolor)
            else:
                if font == None:
                    font = LAODER.FONT[0]
                return pg.font.Font(font, size).render(LAODER.LANG[text], antialias, color, bgcolor)


window = API_8w52764y()


class upaddon:
    def __init__(self) -> None:
        self.uuidpak=f'{uuidpy.rand(0)}.zip'
        tar=threading.Thread(target=self.downjson)
        tar.run()
        zip=zipfile.ZipFile(f'data/download/{self.uuidpak}')
        zip.extractall('data/temp')
        self.dict=jsonpy.FrIn(jsonpy.load('data/temp/EM-V-SW-addon-main/addons.json')).dict
        self.keys=self.dict['keys']
        self.version=self.dict['version']
    def downpack(self,url,name):
        def down():wget.download(url,f'data/download/{name}.zip')
        tar=threading.Thread(target=down)
        tar.run()
        return f'data/download/{name}.zip'
    def update(self,path):
        zip=zipfile.ZipFile(path)
        zip.extractall('data/addon/')
    def addaddons(self,url,name):
        self.update(self.downpack(url,name))
    def downjson(self) -> None:
        wget.download('https://github.com/xubowen159357/EM-V-SW-addon/archive/refs/heads/main.zip',f'data/download/{self.uuidpak}')
def changesetting():
    def downad():
        def choose():
            index = listad.curselection()
            for i in index:
                index=listad.get(i)
            for i in range(len(a.keys)):
                if index==a.dict[a.keys[i]]['name']:
                    a.addaddons(a.dict[a.keys[i]]['dress'],a.keys[i])
        a=upaddon()
        top2 = pg.windowAPI.Toplevel()
        top2.iconbitmap(ICON)
        top2.geometry('600x500')
        top2.title(LAODER.LANG['Setting.downloadaddon'])
        listad=pg.windowAPI.Listbox(top2,width=30,height=20)
        for i in range(len(a.keys)):
            listad.insert(str(i+1),a.dict[a.keys[i]]['name'])
        listad.pack()
        down=pg.windowAPI.Button(top2,text=LAODER.LANG['Downloadaddon.download'],command=choose)
        down.pack()
    def setbutc():
        global LAODER
        a = edit.get('1.0', 'end-1c')
        try:
            jsonpy.Fr(a).dict['$version']['version'][2]
            Lang = jsonpy.Fr(a).dict.get('$Lang')
            Main_Lang = Lang[0]
            Appde_Lang = Lang[1]
            Langs = os.listdir(LAODER.addon.addons['00000000-0000-0000-0000-000000000001'][0]+"/lang")
            Langs: list[str]
            langfile = None
            for i in Langs:
                k = i.split("_")
                if k[0] != Main_Lang:
                    continue
                elif k[1] != Appde_Lang:
                    continue
                else:
                    langfile = i
            if langfile == None:
                raise FileNotFoundError
        except BaseException as er:
            pg.windowAPI.mess.showerror(
                LAODER.LANG['Error'], LAODER.LANG['Error.8w52764y-59gz-jp5s-fd8v-zsywak9rh16w']+f'\n At:{er}')
        open('data/setting/setting.json', 'w', encoding='utf-8').write(a)
        if pg.windowAPI.mess.askyesno(LAODER.LANG['Setting.applynow'], LAODER.LANG['Setting.apply']):
            LAODER = laoders.MAIN()
            pg.display.set_caption(LAODER.LANG['Text.captain'])
    top = pg.windowAPI.Toplevel()
    top.iconbitmap(ICON)
    top.geometry('600x500')
    top.title(LAODER.LANG['MainLob.button.setting'])
    edit = pg.windowAPI.Text(top)
    edit.insert('1.0', LAODER.SETTING.json)
    edit.pack()
    setbut = pg.windowAPI.Button(top, text=LAODER.LANG['Setting.set'], command=setbutc)
    setbut.pack()
    downaddon=pg.windowAPI.Button(top, text=LAODER.LANG['Setting.downloadaddon'], command=downad)
    downaddon.pack()


class transform:
    def scale(win: pg.surface, rect: pg.rect):
        return pg.transform.scale(win, [rect[0]*FULLSUCSSE['full'], rect[1]*FULLSUCSSE['full']])


surfacelook = window.showtext('Text.captain', 45, font=LAODER.FONT[1])
if LAODER.LANG['Lang.type'] == 'zh' and LAODER.SETTING.dict["show-ture-engineer"]:
    surfacelook2 = window.showtext('xu.bw', 25, culertext=1, font=LAODER.FONT[1])
    surfacelook = window.showtext('Text.captain', 45)
if LAODER.LANG['Lang.type'] == 'zh' and not LAODER.SETTING.dict["show-ture-engineer"]:
    surfacelook2 = window.showtext('Text.engineer', 25)
    surfacelook = window.showtext('Text.captain', 45)
elif LAODER.SETTING.dict["show-ture-engineer"]:
    surfacelook2 = window.showtext('xu.bw', 25, culertext=1, font=LAODER.FONT[1])
else:
    # surfacelook=transform.scale(surfacelook,(WID,HEI))
    surfacelook2 = window.showtext('Text.engineer', 25, font=LAODER.FONT[1])
surfacelook = {'sur': surfacelook, 'rect': surfacelook.get_rect(), 'sur2': surfacelook2,
               'rect2': surfacelook2.get_rect()}
surfacelook['rect'].x, surfacelook['rect'].y, surfacelook['rect2'].x, surfacelook['rect2'].y = WID/2 - \
    surfacelook['rect'].w/2, HEI/2-surfacelook['rect'].h/2, WID / \
    2-surfacelook['rect2'].w/2, HEI/2-surfacelook['rect'].h/2+45
settingbutton = pg.load(temp.Path+'/'+temp.file['setting-button'])
mouse = pg.load(temp.Path+'/'+temp.file['mouse']).convert_alpha()
pg.color.Color
pg.surface.Surface.set_palette
pg.Rect.width

class boss:
    def __init__(chess, *args) -> None:
        chess.boss = None
        chess.button = pg.sprite.Group()


class player:
    def __init__(chess, *args) -> None:
        chess.player = pg.sprite.Group()
        chess.button = pg.sprite.Group()


bossG = boss()
playerG = player()


class bossself(pg.sprite.Sprite):
    def __init__(self, imgcik, *groups) -> None:
        try:
            pg.sprite.Sprite.__init__(self)
            self.png = LAODER.addon.bossimage[imgcik][0]
            self.bool = 200
            self.sur = pg.load(self.png).convert_alpha()
            self.sur = {'sur': self.sur, 'bool': window.showtext(
                LAODER.LANG['Play.bool']+':'+str(self.bool), 15, culertext=1)}
            self.rect = self.sur['sur'].get_rect()
            self.size=(80*(self.rect.w/self.rect.h), 80)
            self.rect.w, self.rect.h = window.blit(self.sur['sur'], self.rect, self.size)
            self.gorect = [0, self.rect.height]
            self.alpha = 255
            self.level = 1
            self.timekey = 0
            self.levelchangev = 0
            self.speed = 1
        except:
            global ERROR
            global RUN
            global CAT
            CAT=self
            ERROR = 'Error.epk6fbgw-amsg-we5o-05pz-jybp2bnwm2yl'
            RUN = False

    def levelchange(self):
        if self.levelchangev:
            if self.timekey == 0:
                self.timekey = time_killer['time']
            elif self.timekey+6 == time_killer['time']:
                self.levelchangev = 0
                self.timekey = 0
            if time_killer['time'] <= self.timekey+2:
                text = pg.font.Font(LAODER.FONT[0], 35).render('LOOK OUT L:%d' % self.level, 0, (255, 0, 0), None)
                center = pg.draw.rect(ROOT, (225, 0, 0), [WID/2-200, HEI/2-30, 400, 60], 10).center
                window.blit(text, [center[0]-text.get_rect().w/2, center[1]-text.get_rect().h/2])

    def update(self, tick=0, *args, **kwargs) -> None:
        global REBOOL
        bool = 0
        if time_killer['tick'] == 0:
            self.gorect = [random.randint(self.rect.w, WID-self.rect.w), self.rect.height]
        if self.rect.x < self.gorect[0]:
            self.rect.x += self.speed
        if self.rect.x > self.gorect[0]:
            self.rect.x -= self.speed
        if tick == 1:
            bool = random.randint(REBOOL-10, int(REBOOL+10+REBOOL/10))
        if bool == REBOOL+10+REBOOL/10:
            self.bool -= int(REBOOL*(random.randint(150, 185)/100))
        else:
            self.bool -= bool
        if self.bool <= 0 and self.level < 3:
            self.bool = int(200+200*(100+10*self.level)/100)
            self.level += 1
            self.levelchangev = 1
            self.speed += 2
            REBOOL += int((100+10*self.level)/1000)
            return None
        elif self.bool <= 0:
            self.bool = 0
            bossG.boss.boss = None
            global loop
            loop = 'main'
        self.sur['sur'].set_alpha(self.alpha)
        self.sur['bool'] = window.showtext(LAODER.LANG['Play.bool']+':'+str(self.bool), 15, culertext=1)
        self.sur['leve'] = window.showtext(LAODER.LANG['Play.leve']+':'+str(self.level), 15, culertext=1)
        self.rect.w, self.rect.h = window.blit(self.sur['sur'], self.rect, self.size)
        window.blit(self.sur['bool'], [0, 0], textrcet=self.sur['bool'].get_rect())
        window.blit(self.sur['leve'], [0, 15], textrcet=self.sur['bool'].get_rect(), movetext=[0, -15])
        self.levelchange()


class playerself(pg.sprite.Sprite):
    def __init__(self, imgcik, *groups) -> None:
        try:
            pg.sprite.Sprite.__init__(self)
            self.png = LAODER.addon.playerimage[imgcik][0]
            self.bool = 200
            self.sur = pg.load(self.png)
            self.sur = self.sur
            self.rect = self.sur.get_rect()
            self.rect.w, self.rect.h = window.blit(self.sur, self.rect, (70, 70))
            self.alpha = 255
            self.size = (70, 70)
        except:
            global ERROR
            global RUN
            global CAT
            CAT=self
            ERROR = 'Error.epk6fbgw-amsg-we5o-05pz-jybp2bnwm2yl'
            RUN = False

    def update(self, *args, **kwargs) -> None:
        self.rect.y = HEI-self.rect.h
        if loop != 'play':
            playerG.player.empty()
        if pg.mouse.get_pos()[0] <= pg.display.get_window_size()[0]-self.size[0] and pg.mouse.get_pos()[0] >= 0:
            self.rect.x = pg.mouse.get_pos()[0]
        self.sur.set_alpha(self.alpha)
        self.rect.w, self.rect.h = window.blit(self.sur, self.rect, (70, 70))


class playerbutton(pg.sprite.Sprite):
    def __init__(self, imgcik, *groups) -> None:
        try:
            pg.sprite.Sprite.__init__(self)
            sunds = pg.mixer.Sound('data/sounds/'+LAODER.SOUNDS['button.outgun'])
            sunds.set_volume(0.5)
            THREADS[f'thread{random.randint(2, 6)}'].play(sunds)
            self.png = LAODER.addon.playerimage[imgcik][1]
            self.bool = 200
            self.sur = pg.load(self.png)
            self.sur = self.sur
            self.rect = self.sur.get_rect()
            self.rect.w, self.rect.h = window.blit(self.sur, self.rect, (20, 20))
            self.rect.x, self.rect.y = playerG.player.sprites(
            )[0].rect.centerx, playerG.player.sprites()[0].rect.centery
            self.alpha = 255
            self.speed = 10*60/FPS
            self.angle = 90
            self.size=[40, 40]
            if Schach:
                dx = self.rect.centerx - bossG.boss.rect.centerx
                dy = self.rect.centery - bossG.boss.rect.centery
                self.angle = math.degrees(math.atan2(-dy, dx))+180
                self.gox = math.cos(math.radians(self.angle)) * self.speed
                self.goy = -math.sin(math.radians(self.angle)) * self.speed
            else:
                self.gox = 0
                self.goy = 10
        except BaseException as e:
            global ERROR
            global RUN
            global CAT
            CAT=self
            ERROR = 'Error.epk6fbgw-amsg-we5o-05pz-jybp2bnwm2yl'
            RUN = False

    def update(self, *args, **kwargs) -> None:
        if loop != 'play':
            playerG.button.empty()
        if self.rect.y <= 0:
            playerG.button.remove(self)
        self.rect.x += self.gox
        self.rect.y += -abs(self.goy)
        self.sur.set_alpha(self.alpha)
        self.rect.w, self.rect.h = window.blit(self.sur, self.rect, self.size)


mainloop = {'setting-button': {'sur': settingbutton, "rect": settingbutton.get_rect(), "tick": True,
                               "loop": ["main"],"size":(30, 30)}, 'mouse': {'sur': mouse, "rect": pg.mouse.get_pos}}
# get_center=lambda name :[int(mainloop[name]['rect']().size[0]/2),int(mainloop[name]['rect'].size[1]/2)]
mainloop['setting-button']['rect'].x, mainloop['setting-button']['rect'].y = [WID -
                                                                              mainloop['setting-button']['rect'].width, 0]
listmainloop = ['setting-button']
# imang end

allalpha = 255


def gpu_loop(mouse_pos, keyboard):
    window.blit(pg.font.Font(LAODER.FONT[0], 10).render('FPS: '+str(int(pg.Clock.get_fps())), 0, (0, 0, 0), None), [WID-pg.font.Font(LAODER.FONT[0], 10).render('FPS: '+str(int(
        pg.Clock.get_fps())), 0, (0, 0, 0), None).get_rect().w, HEI-pg.font.Font(LAODER.FONT[0], 10).render('FPS: '+str(int(pg.Clock.get_fps())), 0, (0, 0, 0), None).get_rect().h], textrcet=pg.font.Font(LAODER.FONT[0], 10).render('FPS: '+str(int(pg.Clock.get_fps())), 0, (0, 0, 0), None).get_rect(), movetext=1)
    if loop == 'main':
        for i in listmainloop:
            if pg.draw.rect(ROOT, (225, 255, 225), [WID/2-100, HEI/2-15, 200, 30], 1).collidepoint(mouse_pos):
                pg.draw.rect(ROOT, (125, 255, 125), [WID/2-100, HEI/2-15, 200, 30], 5)
            else:
                pg.draw.rect(ROOT, (225, 255, 225), [WID/2-100, HEI/2-15, 200, 30], 5)
            window.blit(window.showtext('MainLob.button.start', 25), [
                        WID/2-window.showtext('MainLob.button.start', 25).get_rect().w/2, HEI/2-window.showtext('MainLob.button.start', 25).get_rect().h/2])
            window.blit(mainloop[i]['sur'], mainloop[i]['rect'],mainloop[i].get('size'))
    elif loop == 'play':
        bossG.boss.update()
        playerG.player.update()
        try:
            playerG.button.update()
        except BaseException as er:
            print(er)
    if loop != 'play':
        window.blit(mainloop['mouse']['sur'], pg.mouse.get_pos(), [20, 20])


def cpu_loop(mouse_pos, keyboard):
    if loop == 'play':
        spritecollided = len(pg.sprite.spritecollide(bossG.boss, playerG.button, True))
        if spritecollided != 0:
            for i in range(spritecollided):
                bossG.boss.update(tick=1)
        if keyboard[pg.K_b]:
            playerG.button.add(playerbutton('wheel'))


# def touch(mouse_pos:tuple[int,int]):
#    for i in listmainloop:
#        if mainloop[i].get('tick') and mainloop[i]['rect'].collidepoint(mouse_pos):
#            mainloop[i]['sur']=pg.transform.rotate(mainloop[i]['sur'], 10)

def tick(mouse_pos):
    global loop
    if loop == 'main':
        if pg.draw.rect(ROOT, (225, 255, 225), [WID/2-100, HEI/2, 200, 30], 1).collidepoint(mouse_pos):
            loop = 'play'
            bossG.boss = bossself(LAODER.SETTING.dict['image']['boss'])
            playerG.player.add(playerself(LAODER.SETTING.dict['image']['player']))
        else:
            for i in listmainloop:
                if mainloop[i].get('tick') and (loop in mainloop[i].get('loop')) and mainloop[i]['rect'].collidepoint(mouse_pos):
                    changesetting()
    elif loop == 'play':
        playerG.button.add(playerbutton(LAODER.SETTING.dict['image']['player']))


def updata(*Any):
    global RUN
    global WID, HEI
    global loop
    global Schach
    mouse_pos = pg.mouse.get_pos()
    keyboard = pg.key.get_pressed()
    gpu_loop(mouse_pos, keyboard)
    cpu_loop(mouse_pos, keyboard)
    pg.display.flip()
    pg.Clock.tick(FPS)
    root.update()
    for event in pg.event.get():
        if event.type == pg.locals.QUIT:
            if pg.windowAPI.mess.askyesnocancel(LAODER.LANG['Quit.captain'], LAODER.LANG['Quit.quit']):
                RUN = 0
#        elif event.type == pg.VIDEORESIZE:
#            WID = event.w
#            HEI = event.h
#            window = pg.display.set_mode([WID, HEI], pg.SCALED|pg.RESIZABLE)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                if loop == 'play':
                    if pg.windowAPI.mess.askyesno(LAODER.LANG['Quit.captain'], LAODER.LANG['Quit.play.quit']):
                        loop = 'main'
                elif pg.windowAPI.mess.askyesnocancel(LAODER.LANG['Quit.captain'], LAODER.LANG['Quit.quit']):
                    RUN = 0
            if event.key == pg.K_F1:
                if Schach:
                    Schach = 0
                else:
                    Schach = 1
            elif event.key == pg.K_F11 and loop != 'screen':
                if FULLSUCSSE['full'] == 0:
                    FULLSUCSSE['full'] = 1
                    pg.display.set_mode(FULLSUCSSE['max_size'], pg.HWSURFACE | pg.FULLSCREEN)
                    WID, HEI = FULLSUCSSE['max_size']
                else:
                    FULLSUCSSE['full'] = 0
                    pg.display.set_mode(FULLSUCSSE['size'], pg.HWSURFACE)
                    WID, HEI = FULLSUCSSE['size']
        if event.type == pg.MOUSEBUTTONDOWN:
            tick(mouse_pos)
#    touch(mouse_pos)
    time_killer['tick'] += 1
    time_killer['time'] = int(time_killer['time'])+time_killer['tick']/FPS
    if time_killer['tick'] == FPS:
        time_killer['tick'] = 0


surfacelook['sur'].set_alpha(time_killer['clock1'])

while RUN:
    ROOT.fill((225, 225, 225))
    if time_killer['time'] < 4:
        if time_killer['time'] < 2:
            surfacelook['sur'].set_alpha(time_killer['clock1'])
            surfacelook['sur2'].set_alpha(time_killer['clock1'])
            time_killer['clock1'] += 4
        if 2 < time_killer['time']:
            surfacelook['sur'].set_alpha(time_killer['clock1'])
            surfacelook['sur2'].set_alpha(time_killer['clock1'])
            time_killer['clock1'] -= 5
        window.blit(surfacelook['sur'], surfacelook['rect'])
        window.blit(surfacelook['sur2'], surfacelook['rect2'])
        updata()
        continue
    if time_killer['time'] == 4:
        loop = 'main'
# get for key value
    updata()
if ERROR != None:
    pg.windowAPI.mess.showwarning(LAODER.LANG['Error'], f'{LAODER.LANG[ERROR]},report at {CAT}')
os.system(f'del /Q data\\download\\*')
