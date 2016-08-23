#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    # regex = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"
    # puzzle_url = re.findall(r'GET(.*?)HTTP', line)
    with open(filename) as f:
        lines = f.readlines()
        protocol = r'http://'
        hostname = filename.split('_')[1]
        print hostname

        urls = set()
        for line in lines:
            match = re.search(r'\S+(puzzle*).\S+',line)
            if match:
                url = match.group()
                full_url = '{0}{1}{2}'.format(protocol, hostname, url)
                urls.add(full_url)

    return sorted(urls)

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    index_html = "<html><body>[IMG]</body></html>"
    index_img = list()

    for id, img_url in enumerate(img_urls):
        img_id = "img{0}.jpg".format(id)
        dest_dir_img = os.path.join(dest_dir, img_id)
        img_html = "<img src='{0}'>".format(dest_dir_img)
        index_img.append(img_html)

        print('Retrieving... {0}'.format(img_id))
        urllib.urlretrieve(img_url, dest_dir_img)

    index = index_html.replace('[IMG]', ''.join(index_img))
    index_filename = os.path.join(dest_dir, 'index.html')
    with open(index_filename, 'w') as f:
        f.write(index)

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
