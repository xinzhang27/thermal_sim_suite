import os
import subprocess
from pathlib import Path
import nicegui

cmd = [
    r'D:\projects\Programming\abaqus_app\.venv\Scripts\python.exe',
    '-m', 'PyInstaller',
    'main.py',  # your main file with ui.run()
    '--name', 'myapp',  # name of your app
    '--onefile',
    '--hidden-import',
    'matplotlib',
    '--windowed',  # prevent console appearing, only use with ui.run(native=True, ...)
    '--clean',
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'
]

subprocess.call(cmd)
