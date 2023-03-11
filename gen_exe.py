'''
Kai Delsing
03-10-2023

~ ~ GENERATE EXE ~ ~
This program generates a runnable .exe that functions like cli.py, but also packages the
    python interpreter and all dependent libraries
'''

import PyInstaller.__main__

PyInstaller.__main__.run([
    'cli.py',
    '--onefile',
    '--windowed',
    '--icon=./media/peteter.ico',
    '--name=SQI',
    '--distpath=./',
    '--workpath=./.build',
])