# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:40:09 2024

@author: dop24
"""

from pytube import YouTube

link = "https://www.youtube.com/watch?v=usu0XY4QNB0"
yt = YouTube(link)
yt.streams.first().download()
