# Banyl 2021
# Copyright (C) jesus1554 MIT Licence

import eyed3
import eyed3.plugins.art
import requests
import os

# raw = requests.get('https://api.deezer.com/album/302127')

# res = raw.json()
# print(res)


for file_name in os.listdir('exampledir/'):
    print(file_name)

audiofile = eyed3.load("exampledir/Billie Eilish - bad guy.mp3")
# audiofile.tag.images.set(3, open('test-art.jpg','rb').read(), 'image/jpeg')

# audiofile.tag.save()
print(audiofile.tag.title)
