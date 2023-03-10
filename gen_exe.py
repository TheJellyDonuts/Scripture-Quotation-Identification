import PyInstaller.__main__

PyInstaller.__main__.run([
    'cli.py',
    '--onefile',
    '--windowed',
    '--icon=media/peteter.ico',
    '--name=SQI',
    '--distpath=./',
    '--workpath=./.build',
])