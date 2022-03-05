#!/usr/bin/env python
import urllib.parse
from urllib.request import urlopen
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import os
import sys
import requests

# Check argument array length
if len(sys.argv) < 1:
    sys.exit("\nNot enough arguments!")

# Process each argument
for i in range(1, len(sys.argv)):
    # Check if argument is length 24 (channel_id) or 34 (playlist_id)
    if len(sys.argv[i])==24 or len(sys.argv[i])==34:
        mode = 1
        if len(sys.argv[i])>24:
            url = 'https://www.youtube.com/feeds/videos.xml?playlist_id=' + sys.argv[i]
        else:
            mode = 0
            url = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + sys.argv[i]

        try:
            html_page = urlopen(url)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print('The server could not be found!')
        else:
            bs = BeautifulSoup(html_page.read(), 'lxml', from_encoding="utf-8")
            if (mode==0):
                mode_str = "Channel"
                name = bs.find("name").text.strip()
            else:
                mode_str = "Playlist"
                name = bs.find("title").text.strip()

            print()
            print(mode_str + " ID: " + sys.argv[i])
            print(mode_str + " name: " + name)

            published = bs.find("published").text.strip().replace("+00:00", "").replace("T", " ").split()
            print("Publish date: " + published[0])
            print("Publish time: " + published[1])

            print("Last " + mode_str.lower() + " videos")
            list_video = bs.find_all("media:title")
            for video in list_video:
                print("- " + video.text.strip())
    else:
        print("Invalid argument (" + sys.argv[i] + ")")
