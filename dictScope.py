
from multiprocessing.sharedctypes import Value


class dictScope:
    def __init__(self):
        self.dict = {}
        
    def addFunctionOrGlobalVar(self, name : str, value):
        self.dict[name] = value
    
    def addLocal(self, name : str, value, funcI : str, block : str = None):
        funcI = funcI + "Var"
        if block is None:
            try:
                tempData = self.dict[funcI]
                tempData[name] = value
                self.dict[funcI] = tempData
            except:
                self.dict[funcI] = {name : value}
        else:
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
            
    
    def getValue(self, name : str, funcI : str = None, block : str = None):
            if not funcI is None:
                funcI = funcI + "Var"
                if block is None:
                    try:
                        tempData = self.dict[funcI]
                        try:
                            return tempData[name]
                        except:
                            try:
                                return self.dict[name]
                            except:
                                raise ValueError()
                    except:
                        raise ValueError("No Function found in scope or variable not found in function scope.")
                else:
                    try:
                        tempDataFunction = self.dict[funcI]
                        try:
                            tempDataBlock = tempDataFunction[block]
                            try:
                                return tempDataBlock[name]
                            except:
                                try:
                                    return tempDataFunction[name]
                                except:
                                    try:
                                        return self.dict[name]
                                    except:
                                        raise ValueError("No Variable with this name found in scope")
                        except:
                            raise ValueError("No Block found")
                    except:
                        raise ValueError("No Function found")
            else:
                try:
                    return self.dict[name]
                except:
                    raise ValueError("No Variable found in scope.")