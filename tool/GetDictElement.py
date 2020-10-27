def GetDirsDictElement(DirsDict, func):
    print("dfaffff")
    def wrapper(DirsDict, func):

        if not DirsDict:

            print("无子集")
            return

        for k in DirsDict.keys():
            print(k,DirsDict[k])
            func(DirsDict[k])
            return DirsDict(DirsDict[k],func)

    return wrapper(DirsDict, func)