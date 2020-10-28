def GetDirsDictElement(DirsDict, func, basedir=""):

    #print("dfaffff")
    def wrapper(DirsDict,prefix="",basedir=basedir):

        if not DirsDict:

            print("无子集")
            return

        for k in DirsDict.keys():
            prefix = prefix +"//"+ k
            print(prefix, k)
            func(DirsDict[k], basedir)
            wrapper(DirsDict[k], prefix)

    return wrapper(DirsDict)
