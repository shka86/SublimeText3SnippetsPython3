#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pathlib
import shutil
from pathlib import Path as p
from distutils import dir_util as du

# cwd
path_current = pathlib.Path().cwd()
print(path_current)

# cwd shortened
path_current = p().cwd()
print(path_current)

# parent
path_parent = path_current.parent
print(path_parent)

# only current
# only suffix
# recursive
list_dir = path_current.glob("*")
list_dir = path_current.glob("*.py")
list_dir = path_current.glob("**/*")


# path concatinate
# rm dir
# mkdir
path_new = path_current / p("new_dir")

if path_new.is_dir():
    shutil.rmtree(path_new)

path_new.mkdir()

newfile = path_new / p("hoge.txt")
with open(newfile, 'w') as f:
    f.write("test hoge")

path_src = path_new
path_dst = p(str(path_new) + "_")
if path_dst.is_dir():
    shutil.rmtree(path_dst)

# copy tree to tree
du.copy_tree(str(path_src), str(path_dst))


input("hit a key")
