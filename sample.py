#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def main(args):

    tgt = "testfile.txt"

    with open(tgt, 'w') as f:
        f.write("test str")

    with open(tgt, 'r') as f:
        lines = f.readlines()

    for line in lines:
        print(line)

    print("## os")
    import os

    # Bool, file or dir exist?
    print(os.path.exists(tgt))

    # Bool, dir exist?
    print(os.path.isdir(tgt))

    #Bool, file exist?
    print(os.path.isfile(tgt))

    #Bool, symbolic link exist?
    print(os.path.islink(tgt))

    print("## pathlib")
    import pathlib

    # Bool, file or dir exist?
    print(pathlib.Path(tgt).exists())

    # Bool, dir exist?
    print(pathlib.Path(tgt).is_dir())

    #Bool, file exist?
    print(pathlib.Path(tgt).is_file())

    #Bool, symbolic link exist?
    print(pathlib.Path(tgt).is_symlink())

    input("hit a key")

if __name__ == '__main__':

    args = sys.argv
    main(args)
