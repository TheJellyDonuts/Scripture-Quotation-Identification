import PyInstaller.__main__

PyInstaller.__main__.run([
    'cli.py',
    '--onefile',
    '--windowed',
#    '--icon=icon.ico',
    '--name=Scripture-Quotation-Identification',
    '--distpath=./',
    '--workpath=./.build',
])