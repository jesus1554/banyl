# Banyl 2021
# Copyright (C) jesus1554 MIT Licence

import os

import eyed3
import eyed3.plugins.art
import requests
import json
import wget

# raw = requests.get('https://api.deezer.com/album/302127')

# res = raw.json()
# print(res)


def getDir():
    dirpath = input("Give the path of your music directory: ")
    if os.path.isdir(dirpath):
        return dirpath
    else:
        print("U-Oh! The path doesn't exist .-.")
        dirpath = getDir()
        return dirpath


def checkDir(path):
    for file_name in os.listdir(path):
        if file_name.endswith('.mp3'):
            return True
        else:
            return False


def checkSong(userRequest):
    rawResponse = requests.get(
        f'https://api.deezer.com/search?q="{userRequest}"')
    res = json.loads(rawResponse.text)
    if res["total"] == 0:
        print("Song not found")
        return False
    else:
        idSong = res["data"][0]["id"]
        return idSong


def getSong(title):
    targetId = checkSong(title)
    if targetId:
        rawResponse = requests.get(f'https://api.deezer.com/track/{targetId}')
        res = json.loads(rawResponse.text)
        print(res["album"]["title"])
    else:
        pass


def editTags(path):
    for file_name in os.listdir(path):
        if file_name.endswith('.mp3'):
            audiofile = eyed3.load(f"{path}/{file_name}")
            songTitle = file_name.replace('.mp3', '')
            newTags = getSong(songTitle)

            audiofile.initTag()
            # Updating music tags from Deezer.com
            audiofile.tag.artist = newTags["artist"]["name"]
            audiofile.tag.album = newTags["album"]["title"]
            audiofile.tag.album_artist = newTags["artist"]["name"]
            audiofile.tag.title = newTags["title"]

            # Updating art work
            updateArtWork(audiofile, newTags)

            audiofile.tag.save()
        else:
            continue


def updateArtWork(song, tags):
    if os.path.isdir("img-cache"):
        pass
    else:
        os.mkdir("img-cache")

    print(tags["album"])


def separator():
    return print("*" * 50)


if __name__ == "__main__":
    songsDir = getDir()
    dirValidation = checkDir(songsDir)
    if dirValidation:
        editTags(songsDir)
    else:
        print(
            'Sorry, for now, Banyl only accepts folders with all the files in mp3 format.')
