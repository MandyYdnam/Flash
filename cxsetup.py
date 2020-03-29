import cx_Freeze as cx
import sys


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

with open("README.rst", "r") as fh:
    long_description = fh.read()

cx.setup(
    name="flash_parser",
    version='0.1',
    author="Mandeep Dhiman",
    author_email="mandeepsinghdhiman@outlook.com",
    description="A GUI based Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MandyYdnam/",
    packages= ['flash_app'],
    executables=[cx.Executable('flash_app.py',
                                 targetName='flashapp',
                                 icon='flash_hero_icon.ico', base=base)],
    # options={
    #     'build_exe': {
    #         'packages': ["tkinter", "json", "os"],
    #         'includes': ["tkinter", "json"],
    #     }
    # }
)