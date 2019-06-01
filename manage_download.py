#!/usr/bin/env python3.6

import sys,os
import re
import shutil

BASE_DIR = "/Users/sunjingwei/Downloads"
SUFFIX_PATTEN = re.compile(r'''^.*\.([^\.]*)$''')

my_dict = {
        "images":['.png','.jpg','.gif', '.jpeg'],
        "books":['.txt','.epub','.pdf','.mobi'],
        "videos":['.avi','.rmvb','.mp4','.mkv', '.mov'],
        "voices":['.mp3', '.wmv', '.m4a'],
        "docs":['.doc', '.docx', '.html', '.htm', '.ppt', '.pptx','.key', '.xls', '.xlsx', '.csv'],
        "xmind":['.xmind', '.mmap','.mindnode'],
        "archives":['.zip', '.rar', '.exe', '.apk', '.dmg']
        }

def reverse_dict(my_dict):
    result = {}
    for i, key in enumerate(my_dict):
        for v in my_dict[key]:
            result[v] = key
    #print("result=%s"%result)
    return result

def make_dirs(my_dict):
    if os.path.abspath(os.curdir) != BASE_DIR:
        os.chdir(BASE_DIR)
    assert(os.path.abspath(os.curdir) == BASE_DIR)
    for i,key in enumerate(my_dict):
        print("makedir "+ key)
        os.makedirs(key, exist_ok=True)

def move_file(file_name, my_reverse_dict):
    result = re.match(SUFFIX_PATTEN, file_name)
    if (result):
        suffix = result.group(1) if len(result.groups()) >= 1 else None
        print("suffix of %s : %s"% (file_name, suffix))
        my_suffix = "." + suffix
        if my_suffix in my_reverse_dict:
            target_dir = my_reverse_dict["."+suffix]
            print("moving file %s to dir %s"% (file_name, target_dir))
            shutil.move(file_name, target_dir)


def main():
    my_reverse_dict = reverse_dict(my_dict)
    print(my_reverse_dict)
    make_dirs(my_dict)
    os.chdir(BASE_DIR)
    if os.path.abspath(os.curdir)==BASE_DIR:
        for filename in os.listdir('.'):
            if os.path.isfile(filename):
                print("handling" + filename)
                move_file(filename, my_reverse_dict)

if __name__ == "__main__":
    main()
