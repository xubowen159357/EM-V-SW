import json


class Json:
    def __init__(self,Input) -> None:
        self.able=Input
        self.type=type(Input)

class Input:
    def __init__(self, file_path, code='utf-8') -> None:
        self.file=open(file_path,'r',encoding=code)
        self.value=self.file.read()
        self.file.close()

class Output:
    def __init__(self,value) -> None: 
        value=Json(value)
        if value.type==str:
            self.dict=json.loads(value.able)
            self.json=value.able
        elif value.type==dict:
            self.dict=value.able
            self.json=json.dumps(value.able)
        else:
            raise ValueError
        self.dict:dict
        self.json:Json

class IO:
    def Tjson(I):
        return Output(I)
    
    def Fjson(I):
        return Output(I)
