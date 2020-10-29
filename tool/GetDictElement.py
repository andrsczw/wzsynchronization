def GetDirsDictElement(DirsDict, func, BaseDir):

    #print("dfaffff")
    def wrapper(DirsDict, level=-1, prefix=""):
        print(level)

        if not isinstance(DirsDict, dict):
            print('不是字典')

        if not DirsDict:
            print("无子集")



        for k in DirsDict.keys():
            print(level, "  afafaf  ", k)
            if level == -1:
                prefix = ""
            prefix = prefix + "\\" + k
            print("b+prefix:  ", prefix)
            func(prefix,BaseDir)
            wrapper(DirsDict[k], level+1, prefix)

    return wrapper(DirsDict)