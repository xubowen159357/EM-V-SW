class Load:
    def __init__(self, FroderName, jsonPy):
        self.jsonPath=f'data/image/{FroderName}/file.json'
        self.Path=f'data/image/{FroderName}'
        self.dict=jsonPy.Fr(open(self.jsonPath).read()).dict
        self.type='nol'
        self.uuid=self.dict['uuid']
        if self.dict['type']!='killer'and self.dict['type']!='player':
            self.file=self.dict['file']
        elif self.dict['type']=='killer':
            self.type='boss'
            self.dict_boss=jsonPy.Fr(open(self.Path+'/'+self.dict['file']['boss']).read()).dict
            self.bosslist=self.dict_boss['boss']
            self.bossimage={}
            for i in self.bosslist:
                self.bossimage[i]=[self.Path+f'/boss/{i}/'+jsonPy.Fr(open(self.Path+f'/boss/{i}/{i}.json').read()).dict['boss-image'],self.Path+f'/boss/{i}/'+jsonPy.Fr(open(self.Path+f'/boss/{i}/{i}.json').read()).dict['boss-button']]
        elif self.dict['type']=='player':
            self.type='player'
            self.dict_boss=jsonPy.Fr(open(self.Path+'/'+self.dict['file']['player']).read()).dict
            self.playerlist=self.dict_boss['player']
            self.playerimage={}
            for i in self.playerlist:
                self.playerimage[i]=self.Path+f'/player/{i}/'+jsonPy.Fr(open(self.Path+f'/player/{i}/{i}.json').read()).dict['player']

class images:

    def __init__(self) -> None:
        self.images={}

    def add(self, image:Load):
        uuid=image.uuid
        self.images[uuid]=image

