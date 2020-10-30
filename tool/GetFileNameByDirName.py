import os


def GetFileNameByDirName(file_dir):
    files=""
    l=[]
    # for root, dirs, files in os.walk(file_dir):
    #     print("000000000000000",root,dirs,files)
    for n in os.walk(file_dir):
        if n[2] :

            l.append(str(n[0] + "\\" + n[2][0]))

    #l = [n for n in os.walk(file_dir)][0][2]
    print("jjjjjjjjjjjjjj",l)
    return l
    #return files
