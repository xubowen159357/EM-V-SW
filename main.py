from data.code.pygamelocals import pygamelocals as pg
from data.code.jsonPy import jsonPy as jsonpy
from data.code.uuidPy import uuidPy as uuidpy
import random
import laoders
import time
import math
import os


LAODER=laoders.MAIN()
RUN = 1
WID, HEI = 192*5, 108*5
UUID = uuidpy.uuidkey()
FPS = LAODER.SETTING.dict['FPS_MAX']
REBOOL = 10
ICON = 'data/setting/icon.ico'
ERROR=None


root = pg.windowAPI.Tk()
root.title(LAODER.LANG['Text.smellcaptain'])
root.wm_withdraw()

pg.init()
window = pg.display.set_mode([WID, HEI])
pg.display.set_caption(LAODER.LANG['Text.captain'])
pg.display.set_icon(pg.load(ICON))
pg.mouse.set_visible(False)
loop = 'screen'
time_killer = {'tick': 0, 'time': 0, 'clock1': 0}
# imang
temp = LAODER.images.images['7PHKQHQ0-CB90-QYL0-343S-3RRJYKDS1J1Q']
Schach = 0
THREADS={}

for i in range(2,7):
    THREADS['thread'+str(i)]=pg.mixer.Channel(i)


if LAODER.SETTING.dict['$version']['type'] == 'alpha' or LAODER.SETTING.dict['$version']['type'] == 'bate':
    if LAODER.LANG['Lang.type'] != 'zh':
        if not pg.windowAPI.mess.askretrycancel(f'Version {LAODER.SETTING.dict['$version']['type']}', f'You are currently using version {LAODER.SETTING.dict['$version']['type']}, this version usually has a lot of bugs, if you encounter, please do not tell me, because I am busy. Thank you for your cooperation!'):quit()
    else:
        if not pg.windowAPI.mess.askretrycancel(LAODER.SETTING.dict['$version']['type']+' 版本', f'你现在设用的是 {LAODER.SETTING.dict['$version']['type']} 版本, 此版本通常有很多Bug, 如果你遇到了, 请不要告诉我, 因为我很忙。谢谢合作！'):quit()


'''
surfacelook=pg.load(temp[0]+'/'+temp[1]['log'])
surfacelook=pg.transform.scale(surfacelook,(WID,HEI))'''


def showtext(text: str, size: int, color: tuple = (0, 0, 0), font=None, bgcolor: tuple | None = None, antialias: int = 0, culertext=0):
    if culertext:
        if LAODER.LANG['Lang.type'] == 'zh':
            if font == None:font = LAODER.FONT[2]
            return pg.font.Font(font, size).render(text, antialias, color, bgcolor)
        else:
            if font == None:font = LAODER.FONT[0]
            return pg.font.Font(font, size).render(text, antialias, color, bgcolor)
    else:
        enl = ['Text.smellcaptain']
        if LAODER.LANG['Lang.type'] == 'zh' and not text in enl:
            if font == None:font = LAODER.FONT[2]
            return pg.font.Font(font, size).render(LAODER.LANG[text], antialias, color, bgcolor)
        elif text in enl:
            return pg.font.Font(LAODER.FONT[1], size).render(LAODER.LANG[text], antialias, color, bgcolor)
        else:
            if font == None:font = LAODER.FONT[0]
            return pg.font.Font(font, size).render(LAODER.LANG[text], antialias, color, bgcolor)


def changesetting():
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
        if pg.windowAPI.mess.askyesno(LAODER.LANG['Setting.applynow'],LAODER.LANG['Setting.apply']):
            LAODER=laoders.MAIN()
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


surfacelook = showtext('Text.captain', 45, font=LAODER.FONT[1])
if LAODER.LANG['Lang.type'] == 'zh':
    surfacelook2 = showtext('Text.engineer', 25)
    surfacelook = showtext('Text.captain', 45)
elif LAODER.SETTING.dict.get("show-ture-engineer"):
    surfacelook2 = showtext('xu.bw', 25, culertext=1, font=LAODER.FONT[1])
else:
    # surfacelook=pg.transform.scale(surfacelook,(WID,HEI))
    surfacelook2 = showtext('Text.engineer', 25, font=LAODER.FONT[1])
surfacelook = {'sur': surfacelook, 'rect': surfacelook.get_rect(), 'sur2': surfacelook2,
            'rect2': surfacelook2.get_rect()}
surfacelook['rect'].x, surfacelook['rect'].y, surfacelook['rect2'].x, surfacelook['rect2'].y = WID/2 - \
    surfacelook['rect'].w/2, HEI/2-surfacelook['rect'].h/2, WID / \
    2-surfacelook['rect2'].w/2, HEI/2-surfacelook['rect'].h/2+45
settingbutton = pg.load(temp.Path+'/'+temp.file['setting-button'])
settingbutton = pg.transform.scale(settingbutton, (30, 30))
mouse = pg.load(temp.Path+'/'+temp.file['mouse'])
mouse = pg.transform.scale(mouse, (20, 20))
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
    def __init__(self, imgcik, pak=LAODER.images.images['BJ0SXVEY-4Q00-871E-P0LA-VGQPTGEBS4DH'], *groups) -> None:
        pg.sprite.Sprite.__init__(self)
        self.png = pak.bossimage[imgcik][0]
        self.bool = 200
        self.sur = pg.load(self.png).convert_alpha()
        self.sur = {'sur': pg.transform.scale(
            self.sur, (80*0.648, 80)), 'bool': showtext(LAODER.LANG['Play.bool']+':'+str(self.bool), 15, culertext=1)}
        self.rect = self.sur['sur'].get_rect()
        self.gorect = [0, self.rect.height]
        self.alpha = 255
        self.level = 1
        self.timekey = 0
        self.levelchangev = 0
        self.speed = 1

    def levelchange(self):
        try:
            if self.levelchangev:
                if self.timekey == 0:
                    self.timekey = time_killer['time']
                elif self.timekey+6 == time_killer['time']:
                    self.levelchangev = 0
                    self.timekey = 0
                if time_killer['time'] <= self.timekey+2:
                    text = pg.font.Font(LAODER.FONT[0], 35).render('LOOK OUT L:%d' % self.level, 0, (255, 0, 0), None)
                    center = pg.draw.rect(window, (225, 0, 0), [WID/2-200, HEI/2-30, 400, 60], 10).center
                    window.blit(text, [center[0]-text.get_rect().w/2, center[1]-text.get_rect().h/2])
        except:
            global ERROR
            global RUN
            ERROR='Error.epk6fbgw-amsg-we5o-05pz-jybp2bnwm2yl'
            RUN=False

    def update(self, tick=0, *args, **kwargs) -> None:
        global REBOOL
        bool = 0
        if time_killer['tick'] == 0:
            self.gorect = [random.randint(self.rect.width, WID-self.rect.w), self.rect.height]
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
        self.sur['bool'] = showtext(LAODER.LANG['Play.bool']+':'+str(self.bool), 15, culertext=1)
        self.sur['leve'] = showtext(LAODER.LANG['Play.leve']+':'+str(self.level), 15, culertext=1)
        window.blit(self.sur['sur'], self.rect)
        window.blit(self.sur['bool'], (0, 0))
        window.blit(self.sur['leve'], (0, 15))
        self.levelchange()


class playerself(pg.sprite.Sprite):
    def __init__(self, imgcik, pak=LAODER.images.images['G12WQ9GV-X0Z0-HFX3-3Y9O-LQ0TCEZCPFWR'], *groups) -> None:
        try:
            pg.sprite.Sprite.__init__(self)
            self.png = pak.playerimage[imgcik]
            self.bool = 200
            self.sur = pg.load(self.png).convert_alpha()
            self.sur = pg.transform.scale(self.sur, (70, 70))
            self.rect = self.sur.get_rect()
            self.rect.y = HEI-self.rect.height
            self.alpha = 255
        except:
            global ERROR
            global RUN
            ERROR='Error.epk6fbgw-amsg-we5o-05pz-jybp2bnwm2yl'
            RUN=False

    def update(self, *args, **kwargs) -> None:
        if loop != 'play':
            playerG.player.empty()
        if pg.mouse.get_pos()[0] <= WID-self.rect.w and pg.mouse.get_pos()[0] >= 0:
            self.rect.x = pg.mouse.get_pos()[0]
        self.sur.set_alpha(self.alpha)
        window.blit(self.sur, self.rect)


class playerbutton(pg.sprite.Sprite):
    def __init__(self, imgcik, pak=LAODER.images.images['G12WQ9GV-X0Z0-HFX3-3Y9O-LQ0TCEZCPFWR'], *groups) -> None:
        try:
            pg.sprite.Sprite.__init__(self)
            THREADS['thread2'].play(pg.mixer.Sound('data/sounds/'+LAODER.SOUNDS['button.outgun']).set_volume(0.5))
            self.png = pak.playerimage[imgcik]
            self.bool = 200
            self.sur = pg.load(self.png).convert_alpha()
            self.sur = pg.transform.scale(self.sur, (20, 20))
            self.rect = self.sur.get_rect()
            self.rect.x, self.rect.y = playerG.player.sprites()[0].rect.centerx, playerG.player.sprites()[0].rect.centery
            self.alpha = 255
            self.speed = 10
            self.angle = 90
            if Schach:
                dx = self.rect.centerx - bossG.boss.rect.centerx
                dy = self.rect.centery - bossG.boss.rect.centery
                self.angle = math.degrees(math.atan2(-dy, dx))+180
            self.gox = math.cos(math.radians(self.angle)) * self.speed
            self.goy = -math.sin(math.radians(self.angle)) * self.speed
        except:
            global ERROR
            global RUN
            ERROR='Error.epk6fbgw-amsg-we5o-05pz-jybp2bnwm2yl'
            RUN=False

    def update(self, *args, **kwargs) -> None:
        if loop != 'play':
            playerG.button.empty()
        if self.rect.y <= 0:
            playerG.button.remove(self)
        self.rect.x += self.gox
        self.rect.y += -abs(self.goy)
        self.sur.set_alpha(self.alpha)
        window.blit(self.sur, self.rect)


mainloop = {'setting-button': {'sur': settingbutton, "rect": settingbutton.get_rect(), "tick": True,
                            "loop": ["main"]}, 'mouse': {'sur': mouse, "rect": pg.mouse.get_pos}}
# get_center=lambda name :[int(mainloop[name]['rect']().size[0]/2),int(mainloop[name]['rect'].size[1]/2)]
mainloop['setting-button']['rect'].x, mainloop['setting-button']['rect'].y = [WID -
                                                                            mainloop['setting-button']['rect'].width, 0]
listmainloop = ['setting-button']
# imang end

allalpha = 255


def gpu_loop(mouse_pos, keyboard):
    window.blit(pg.font.Font(LAODER.FONT[0], 10).render('FPS: '+str(int(pg.Clock.get_fps())), 0, (0, 0, 0), None), [WID-pg.font.Font(LAODER.FONT[0], 10).render('FPS: '+str(int(
        pg.Clock.get_fps())), 0, (0, 0, 0), None).get_rect().w, HEI-pg.font.Font(LAODER.FONT[0], 10).render('FPS: '+str(int(pg.Clock.get_fps())), 0, (0, 0, 0), None).get_rect().h])
    if loop == 'main':
        for i in listmainloop:
            if pg.draw.rect(window, (225, 255, 225), [WID/2-100, HEI/2-15, 200, 30], 1).collidepoint(mouse_pos):
                pg.draw.rect(window, (125, 255, 125), [WID/2-100, HEI/2-15, 200, 30], 5)
            else:
                pg.draw.rect(window, (225, 255, 225), [WID/2-100, HEI/2-15, 200, 30], 5)
            window.blit(showtext('MainLob.button.start', 25), [
                        WID/2-showtext('MainLob.button.start', 25).get_rect().w/2, HEI/2-showtext('MainLob.button.start', 25).get_rect().h/2])
            window.blit(mainloop[i]['sur'], mainloop[i]['rect'])
    elif loop == 'play':
        bossG.boss.update()
        playerG.player.update()
        try:
            playerG.button.update()
        except BaseException as er:
            print(er)
    if loop != 'play':
        window.blit(mainloop['mouse']['sur'], mainloop['mouse']['rect']())


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

def tick(mouse_pos: tuple[int, int]):
    global loop
    if loop == 'main':
        if pg.draw.rect(window, (225, 255, 225), [WID/2-100, HEI/2, 200, 30], 1).collidepoint(mouse_pos):
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
            elif event.key == pg.K_F1:
                if Schach:
                    Schach = 0
                else:
                    Schach = 1
        if event.type == pg.MOUSEBUTTONDOWN:
            tick(mouse_pos)
#    touch(mouse_pos)
    time_killer['tick'] += 1
    time_killer['time'] = int(time_killer['time'])+time_killer['tick']/FPS
    if time_killer['tick'] == FPS:
        time_killer['tick'] = 0


surfacelook['sur'].set_alpha(time_killer['clock1'])

while RUN:
    window.fill((225, 225, 225))
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
if ERROR!=None:pg.windowAPI.mess.showwarning(LAODER.LANG['Error'],LAODER.LANG[ERROR])
