import os


def GetDirectories(file_dir, **dock):
    """
    Get the root name files and dirs
    获取根文件和目录及当前所在的目录
    :param file_dir:root of the scan dirs 当前查询的目录
    """
    #print(os.walk(file_dir))
    l = [n for n in os.walk(file_dir)][0]
    if len(l) > 0:
        print(l)
        #是否有文件夹
        if len(l[1]) > 0:
            print("有值")
            tmp={}
            for i in l[1]:
                print(i)

                tmp[i] = GetDirectories(file_dir+"\\"+i,dock=dock)
                dock[i] = tmp


        else:
            print("没值")
        return dock
