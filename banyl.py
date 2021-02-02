# -*- coding: utf-8 -*-


# Banyl 2021
# Copyright (C) jesus1554 MIT Licence

import os

import eyed3
import requests
import json
import wget
import shutil
from termcolor import colored
from extras import *

successFiles = 0
ignoredFiles = 0
notFoundFiles= 0

def getDir():
    dirpath = input(f"{infoStr} Give the path of your music directory: ")
    if os.path.isdir(dirpath):
        return dirpath
    else:
        print(colored("[⚠] Whoops! The path doesn't exist, try again!", 'red'))
        dirpath = getDir()
        return dirpath


def checkSong(userRequest):
    global notFoundFiles

    rawResponse = requests.get(
        f'https://api.deezer.com/search?q="{userRequest}"')
    res = json.loads(rawResponse.text)
    if res["total"] == 0:
        print(colored("[⚠] Song not found :(", 'red'))
        notFoundFiles += 1
        return False
    else:
        idSong = res["data"][0]["id"]
        return idSong


def getSong(title):

    targetId = checkSong(title)
    if targetId:
        print(f'{infoStr} Fetching information of {title} from Deezer')

        rawResponse = requests.get(f'https://api.deezer.com/track/{targetId}')
        res = json.loads(rawResponse.text)
        return res
    else:
        return False


def editTags(path):
    global successFiles, ignoredFiles

    print(f'{infoStr} Working on {path}')

    for file_name in os.listdir(path):
        if file_name.endswith('.mp3'):
            print(f'{infoStr} Opening {file_name} ...')

            audiofile = eyed3.load(f"{path}/{file_name}")
            songTitle = file_name.replace('.mp3', '')
    
            newTags = getSong(songTitle)

            if newTags:
                audiofile.tag.clear()
                audiofile.initTag()

                # Updating music tags from Deezer.com
                audiofile.tag.artist = newTags["artist"]["name"]
                audiofile.tag.album = newTags["album"]["title"]
                audiofile.tag.album_artist = newTags["artist"]["name"]
                audiofile.tag.title = newTags["title"]
                audiofile.tag.track_num = newTags["track_position"]

                # Release Year
                rawReleaseDate = newTags["release_date"]
                releaseDate = rawReleaseDate.split('-')
                audiofile.tag.release_date = releaseDate[0]
                audiofile.tag.recording_date = releaseDate[0]
                
                print(f'{infoStr} The basic tags are set!')

                # Updating art work
                updateArtWork(audiofile, newTags)

                audiofile.tag.save()
                print(f'{successStr} All the tags from {newTags["title"]} are set!')
                
                successFiles += 1

                separator('green')

            else:
                pass
        else:
            print(f"{warningStr} {file_name} is not a compatible file extension. Skipping...")
            ignoredFiles += 1

            pass


def updateArtWork(song, tags):
    if os.path.isdir("img-cache"):
        pass
    else:
        os.mkdir("img-cache")

    # Download ArtWork
    print(f'{infoStr} Fetching the album cover of {tags["title"]}')
    wget.download(tags["album"]["cover_big"], bar=False, out='img-cache')

    # Renaming
    os.rename('img-cache/500x500-000000-80-0-0.jpg',
              f'img-cache/{tags["id"]}.jpg')
    # Apply changes
    song.tag.images.set(
        3, open(f'img-cache/{tags["id"]}.jpg', 'rb').read(), 'image/jpeg')
    song.tag.save()


if __name__ == "__main__":
    # Init Welcome!
    initWelcome()

    separator('cyan')

    songsDir = getDir()
    editTags(songsDir)
    print(colored('[✔] All the music files was edited. Done!', 'green'))
    print(f'{successStr} {successFiles} was correctly edited.')
    print(f'{warningStr} {ignoredFiles} was ignored.')
    print(f'{dangerStr} {notFoundFiles} was not found.')
    print(f'{infoStr} Deleting cache...')
    
    shutil.rmtree('img-cache')
    
