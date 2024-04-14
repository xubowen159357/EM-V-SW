class Load:
    def __init__(self, FroderName, jsonPy):
        self.jsonPath=f'data/addon/{FroderName}/{FroderName}.json'
        self.Path=f'data/addon/{FroderName}'
        self.dict=jsonPy.Fr(open(self.jsonPath).read()).dict
        if self.dict.get('type')=='main':self.Reduce=True
        else:self.Reduce=False
        self.name=FroderName
        self.file=self.dict.get('file')
        if self.file:
            self.forder=self.file.get('forder')
        self.uuid=self.dict['uuid']
        self.type='DEF'
        if self.dict.get('pack.type')=='boss':
            self.type='BOSS'
            self.bossimage=['data/addon/%s/%s'%(FroderName,self.dict['boss-image']),'data/addon/%s/%s'%(FroderName,self.dict['boss-button'])]
        if self.dict.get('pack.type')=='player':
            self.type='PLAYER'
            self.playerimage=['data/addon/%s/%s'%(FroderName,self.dict['player']),'data/addon/%s/%s'%(FroderName,self.dict['button'])]

class addons:

    def __init__(self) -> None:
        self.addons={}
        self.bossimage={}
        self.playerimage={}

    def add(self, addon:Load):
        uuid=addon.uuid
        filename=addon.name
        file=addon.Path
        if addon.type=='BOSS':
            self.bossimage[addon.dict['pack.name']]=addon
        if addon.type=='PLAYER':
            self.playerimage[addon.dict['pack.name']]=addon
        self.addons[uuid]=(file, filename, addon)

