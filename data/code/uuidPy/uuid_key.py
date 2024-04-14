from .uuidPy import *

class uuidkey:
    def __init__(self) -> None:
        self.value={}
    
    def add(self, name, uuid):
        self.value[name]=uuid
    
    def deluuid(self, name):
        del self.value[name]
    
    def change(self, name, uuid):
        self.value[name]=uuid
    
    def uuid_fand(self,uuid):
        l=list(self.value.items())
        i:list[str]
        for i in l:
            if i[1] == uuid:
                return i[0]
        return Null('No found.')
    
    def str_fand(self,string:str)->str:
        try:return self.value[string]
        except:return Null('No found.')
    
    def allitem(self):
        return list(self.value.items())
