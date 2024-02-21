class Load:
    def __init__(self, FroderName, jsonPy):
        self.jsonPath=f'data/addon/{FroderName}/{FroderName}.json'
        self.Path=f'data/addon/{FroderName}'
        self.dict=jsonPy.Fr(open(self.jsonPath).read()).dict
        if self.dict['type']=='main':self.Reduce=True
        else:self.Reduce=False
        self.name=FroderName
        self.file=self.dict.get('file')
        self.forder=self.file.get('forder')
        self.uuid=self.dict['uuid']

class addons:

    def __init__(self) -> None:
        self.addons={}

    def add(self, addon:Load):
        uuid=addon.uuid
        filename=addon.name
        file=addon.Path
        self.addons[uuid]=(file, filename, addon)

