import os


def GetFileNameByDirName(file_dir,basedir):
    files=""
    l=[]
    # for root, dirs, files in os.walk(file_dir):
    #     print("000000000000000",root,dirs,files)
    for n in os.walk(file_dir):
        print("n:   ",n)
        if n[2] :
            if len(n[2])>1:
                for v in n[2]:
                    if len(n[0].replace(basedir,""))>=2:
                        print("str(n[0] + " " + n[2])  ",str(n[0] + "\\" + v))
                        l.append(str(n[0] + "\\" + v).replace(basedir, ""))
                    else:
                        tem = str(n[0] + v).replace(basedir, "")
                        l.append(tem)
            elif len(n[0].replace(basedir,""))>=2:
                l.append(str(n[0] + "\\" + n[2][0]).replace(basedir, ""))

            else:
                tem = str(n[0] + n[2][0]).replace(basedir, "")
                l.append(tem)

    #l = [n for n in os.walk(file_dir)][0][2]
    print("jjjjjjjjjjjjjj",l)
    return l
    #return files
