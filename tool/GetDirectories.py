import os


def GetDirectories(file_dir):
    """
    Get the root name files and dirs
    获取根文件和目录及当前所在的目录
    :param file_dir:root of the scan dirs 当前查询的目录
    """
    return [n for n in os.walk(file_dir)][0]
