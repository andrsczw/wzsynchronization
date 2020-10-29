import os


def GetFileNameByDirName(file_dir):
    files=""
    # for root, dirs, files in os.walk(file_dir):
    #     print("000000000000000",root,dirs,files)
    l = [n for n in os.walk(file_dir)][0][2]
    print("jjjjjjjjjjjjjj",l)
    return l
    #return files
