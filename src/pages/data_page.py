import subprocess

from nicegui import app, ui


def calculate(filepath) -> subprocess.Popen:
    # copy_cmd = 'cp toolkit/* {}'.format(filepath.value)
    # subprocess.call(copy_cmd, shell=True)
    my_cmd = 'abaqus cae noGUI script=auto_MMC_FC.py'
    proc = subprocess.Popen(
        my_cmd,
        cwd=filepath.value,
        shell=True
    )
    return proc


def content() -> None:
    ui.label("Home Page")
