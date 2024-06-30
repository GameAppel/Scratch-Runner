from cx_Freeze import setup, Executable

base = "Win32GUI"

setup(
    name="SCR",
    version="1.0",
    description="Scratch Runner",
    author="michaelwangdeming",
    executables=[Executable("SCR.py", base=base, icon="games.ico")]
)