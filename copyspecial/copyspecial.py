#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special
import commands
import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""


# +++your code here+++
# Write functions and modify main() to call them
def list_all(dest_dir, todir='', tozip='', zipfilename='tmp.zip'):

    list_files_found = list()
    for dirname, dirnames, filenames in os.walk(dest_dir):
        for filename in filenames:
            match = re.search(r'(.*?)(__)(.*)(__)(.*?)', filename)
            if match:
                list_files_found.append(os.path.join(dirname, filename))

    if todir:
        create_dir(todir)
        for file_found in list_files_found:
            shutil.copy(file_found, todir)
    elif tozip:
        create_dir(tozip)
        file_names = ' '.join(list_files_found)
        external_command = "zip -j {0} {1}".format(zipfilename, file_names)
        print("Command I'm going to do: {0}").format(external_command)
        (status, output) = commands.getstatusoutput(external_command)
        if status:
            sys.stderr.write(output)
            sys.exit(1)
        print output
    else:
        for file_found in list_files_found:
            print file_found

def create_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)
    else:
        # +++your code here+++
        # Call your functions
        dest_dir = args[0]
        list_all(dest_dir, todir, tozip)

if __name__ == "__main__":
    main()
