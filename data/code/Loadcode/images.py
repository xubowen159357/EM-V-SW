class Load:
    def __init__(self, FroderName, jsonPy):
        self.jsonPath=f'data/image/{FroderName}/file.json'
        self.Path=f'data/image/{FroderName}'
        self.dict=jsonPy.Fr(open(self.jsonPath).read()).dict
        self.type='nol'
        self.uuid=self.dict['uuid']
        if self.dict['type']!='killer'and self.dict['type']!='player':
            self.file=self.dict['file']

class images:

    def __init__(self) -> None:
        self.images={}

    def add(self, image:Load):
        uuid=image.uuid
        self.images[uuid]=image

