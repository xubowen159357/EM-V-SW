from . import local

def load(path:str,code='utf-8') -> local.Input:
    return local.Input(path,code)

def ToIn(In:local.Input) -> local.Output:
    return local.IO.Tjson(In.value)

def FrIn(In:local.Input) -> local.Output:
    return local.IO.Fjson(In.value)

def To(In:dict) -> local.Output:
    return local.IO.Tjson(In)

def Fr(In:local.Json) -> local.Output:
    return local.IO.Fjson(In)