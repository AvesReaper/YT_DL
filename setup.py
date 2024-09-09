from cx_Freeze import setup, Executable

executables = [Executable('main.py', base='Win32GUI', icon='188987.ico')]

setup(
    name='SG_YTdown',
    version='0.1',
    description='Used to download youtube vids',
    executables=executables
)
