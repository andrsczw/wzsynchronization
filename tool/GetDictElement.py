def GetDirsDictElement(DirsDict, func):
    def wrapper(DirsDict, func):
        if not DirsDict:
            print("无子集")
            return
        for k in DirsDict.keys():
            func(DirsDict[k])
            DirsDict(DirsDict[k],func)

    return wrapper()