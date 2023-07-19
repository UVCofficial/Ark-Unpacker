# -*- coding: utf-8 -*-
# Copyright (c) 2022-2023, Harry Huang
# @ BSD 3-Clause License
import os
'''
包含一些常用的文件操作函数
'''

def Delete_File_Dir(dirName:str):
    '''
    ## Delete a Dir
    #### 删除一个文件夹
    :param dirName: Path of the dir;
    :returns: (bool) Execution result;
    '''
    if os.path.isfile(dirName):
        #若是文件
        try:
            os.remove(dirName)
        except:
            print('  错误：删除文件失败', dirName)
            return False
    elif os.path.isdir(dirName):
        #若是文件夹
        for item in os.listdir(dirName):
            tf = os.path.join(dirName,item)
            Delete_File_Dir(tf) #递归调用
        try:
            os.rmdir(dirName)
        except:
            print('  错误：删除目录失败', dirName)

def mkdir(path:str, echo:bool=False):
    '''
    ## Create a Dir
    #### 创建一个文件夹
    :param path: Path of the new dir;
    :param echo: Echo info;
    :returns: (bool) Execution result;
    '''
    path = path.strip().strip('/').rstrip('\\')
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            if echo:
                if len(path) > 24:
                    print(f'  目录已创建 ...{path[-20:]}')
                else:
                    print(f'  目录已创建 {path}')
            return True
        except:
            #错误
            if echo:
                print("  目录创建失败")
            return False
    else:
        #目录已存在
        return False

def get_dir_size(path:str):
    '''
    ## Get the Size of a Dir
    #### 获取一个目录的大小
    :param path: Path of the dir;
    :returns: (int) Size in Byte;
    '''
    size = 0
    lst = os.listdir(path)
    for el in lst:
        new = path+'\\'+el
        if os.path.isfile(new):
            size += os.path.getsize(new)
        else:
            size += get_dir_size(new)
    return size

def get_filelist(path:str, max_depth=0, only_dirs=False):
    '''
    ## Get a list containing all the sub dirs (and files) in the given dir
    #### 获取指定目录中的所有子文件夹（和文件）的列表
    :param path: Path of the specified parent dir;
    :param max_depth: Max searching depth, 0 for unlimited;
    :param only_dirs: Whether to exclude files;
    :returns: (list) A list of file paths;
    '''
    max_depth = int(max_depth)
    lst = []
    for i in os.listdir(path):
        i = os.path.join(path, i)
        if os.path.isdir(i):
            lst.append(i)
            if max_depth == 0 or max_depth > 1:
                lst.extend(get_filelist(i, max_depth - 1))
        elif not only_dirs and os.path.isfile(i):
            lst.append(i)
    return lst

def get_path_authority(path:str):
    '''
    ## Judge Path Accessibility
    #### 判断路径可访问性
    :param path: Path;
    :returns: (bool) Result;
    '''
    if os.path.exists(path)\
        and os.access(path,os.X_OK|os.W_OK|os.R_OK):
        return True
    else:
        return False
