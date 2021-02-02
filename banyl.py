# Banyl 2021
# Copyright (C) jesus1554 MIT Licence

import os

import eyed3
import requests
import json
import wget
import shutil
from termcolor import colored


def getDir():
    dirpath = input("Give the path of your music directory: ")
    if os.path.isdir(dirpath):
        return dirpath
    else:
        print("U-Oh! The path doesn't exist .-.")
        dirpath = getDir()
        return dirpath


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
        return res
    else:
        pass


def editTags(path):
    for file_name in os.listdir(path):
        if file_name.endswith('.mp3'):
            audiofile = eyed3.load(f"{path}/{file_name}")
            songTitle = file_name.replace('.mp3', '')
            newTags = getSong(songTitle)

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

            # Updating art work
            updateArtWork(audiofile, newTags)

            audiofile.tag.save()
        else:
            print(f"{file_name} is not a compatible file extension. Skipping...")
            pass


def updateArtWork(song, tags):
    if os.path.isdir("img-cache"):
        pass
    else:
        os.mkdir("img-cache")

    # Download ArtWork
    wget.download(tags["album"]["cover_big"], 'img-cache')

    # Renaming
    os.rename('img-cache/500x500-000000-80-0-0.jpg',
              f'img-cache/{tags["id"]}.jpg')
    print('\n')

    # Apply changes
    song.tag.images.set(
        3, open(f'img-cache/{tags["id"]}.jpg', 'rb').read(), 'image/jpeg')
    song.tag.save()


def separator():
    return print("*" * 50)


if __name__ == "__main__":

    songsDir = getDir()
    editTags(songsDir)
    print('All Done!')
    print('Deleting cache...')
    shutil.rmtree('img-cache')
    
