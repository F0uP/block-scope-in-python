
from multiprocessing.sharedctypes import Value


class dictScope:
    def __init__(self):
        self.dict = {}
        
    def addFunctionOrGlobalVar(self, name : str, value):
        self.dict[name] = value
    
    def nameInUpperBlock(self, name, funcDict, block):
        for i in range(1,int(block)):
            try:
                if name in funcDict[i]:
                    return i
            except:
                return None
        return None
        
    def addLocal(self, name : str, value, funcI : str, block : int = None):
        funcI = funcI + "Var"
        if block is None:
            if name in self.dict:
                self.dict[name] = value
                return
            try:
                tempData = self.dict[funcI]
                tempData[name] = value
                self.dict[funcI] = tempData
            except:
                self.dict[funcI] = {name : value}
        else:
            x = self.nameInUpperBlock(name, self.dict[funcI], block)
            if name in self.dict:
                self.dict[name] = value
                return
            elif name in self.dict[funcI]:
                self.dict[funcI][name] = value
                return
            elif x is not None:
                self.dict[funcI][x][name] = value
                return
            try:
                tempDataFunction = self.dict[funcI]
                try:
                    tempDataBlock = tempDataFunction[block]
                    tempDataBlock[name] = value
                    self.dict[funcI][block] = tempDataBlock
                except:
                    tempDataFunction[block] = {name : value}
                    self.dict[funcI] = tempDataFunction
            except:
                self.dict[funcI] = {block : {name : value}}
            
    
    def getValue(self, name : str, funcI : str = None, block : int = None):
        if funcI is None:
            if name in self.dict:
                return self.dict[name]
            else:
                raise ValueError("Globally not found Variable " + name + ".")
        else:
            funcI = funcI + "Var"
            if block is None:
                if name in self.dict[funcI]:
                    return self.dict[funcI][name]
                elif name in self.dict:
                    return self.dict[name]
                else:
                    raise ValueError("Variable " + name + " not found global or in given Function.")
            else:
                x = self.nameInUpperBlock(name, self.dict[funcI], block)
                if x is None:
                    if name in self.dict[funcI]:
                        return self.dict[funcI][name]
                    elif name in self.dict:
                        return self.dict[name]
                    else:
                        raise ValueError("Variable " + name + " not found global or in given Function.")
                else:
                    return self.dict[funcI][x][name]