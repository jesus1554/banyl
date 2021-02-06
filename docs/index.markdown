---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Banyl Documentation
---
# Banyl Docs

Hey! 👋 This is Banyl, an easy-to-use tool to complete all the tags in your music catalog.

Banyl searches for mp3 files in a folder indicated by you and completes all the available information of your favorite songs from the API of Deezer.

## Get Started
---

## Installation for Linux and Mac

To install Banyl you have to download the executable file. You can find it in the button below.

[Download Linux Executable](https://github.com/jesus1554/banyl/releases/download/v0.5/banyl){: .btn .btn-blue }

That's it!

## Installation for Windows

There are two different options to install Banyl. The repository of the Windows version is [here](https://github.com/jesus1554/banyl-win).

### Option 1 (recommended)

Download the executable file, the link is down below.

[Download Windows .EXE](https://github.com/jesus1554/banyl-win/releases/download/v0.5/banyl.exe){: .btn .btn-blue }

Then, you have to do some configurations in your antivirus. The only that you have to do is put the .EXE file in the ignored list or whitelist of your antivirus.

Why? I use [PyInstaller](http://www.pyinstaller.org/) to compile my code and transform it into a .EXE file. You can find a tutorial to do that with Windows Defender and Avast. Unfortunately, many people made so many viruses using PyInstaller, so the AV systems detect it as a dangerous Trojan. But don't worry! You can check all the [source code](https://github.com/jesus1554/banyl-win). There's no malware in Banyl.

### Option 2

If you don't want or cannot put Banyl as an ignored file by your antivirus. You can still use it. But the installation is a little trickier.

1. First that you have to do is check if you have Python installed in your machine. To do that you can go to CMD and type this:

    ```bash
    python --version
    ```

    If the response was something like this you have Python installed (The version must be higher than 3.8)

    ```powershell
    Python 3.9.1
    ```

    If the response was something like this it looks like you don't have python installed in your system. You can install it from the [Microsoft Store](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7) or on their [official website](https://www.python.org/downloads/windows/).

    ```powershell
    'python' it is not recognized as an internal or external command, executable program or batch file.
    ```

2. Once you have correctly installed Python you need to download the source code. It's on a .zip, so you have to decompress it.

    [Download Source Code](https://github.com/jesus1554/banyl-win/archive/v0.5.zip){: .btn .btn-blue}

    That's it. Now you have Banyl.

## Usage
---

## Linux and Mac

Just execute the file with your music path directory as an argument. The path is an obligatory argument.

### Example:

```bash
./banyl /home/user/music
```

## Windows (apply for installation number one)

Go to CMD, then go to the directory that contains the file "banyl.exe" and execute it like this.

```powershell
banyl.exe
```

Then, you have to write or paste the exact path of the target music directory.

## Windows (apply for installation number two)

Once you have the .zip file uncompressed. You have to open an CMD window and go to the directory of the .zip file. To execute the program you have to write this.

```powershell
python banyl.py
```

Then, you have to write or paste the exact path of the target music directory.

That's it!

## Contribute
---

You can find the main repo [here](https://github.com/jesus1554/banyl), and the Windows version [here](https://github.com/jesus1554/banyl-win). I'm so open to the feedback so don't doubt and give me all your thoughts on the issues tab on GitHub!

## License
---

Banyl is distributed by an [MIT License](https://github.com/jesus1554/banyl/tree/master/LICENSE).

## Author
---

Banyl was created by [Jesús Flores Espinoza](https://jesus1554.github.io)
