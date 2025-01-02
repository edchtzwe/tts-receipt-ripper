# TTS Receipt Ripper

## Installation
### Windows (Console)
- You will need to Download the official Python3 package from https://www.python.org/downloads/
- Follow the steps and make sure you choose to register to PATH
- Go to the project folder where you can see main.py and start a command console
- Start the app with ```python3 main.py```
### Windows (exe)
- You will need this installed, to check, in a comamnd console, type `python3 -m pip --version`
- If it's not installed, you can do it by typing `python3 -m ensurepip --upgrade`
- Then install this tool by typing `python3 -m pip install pyinstaller`
- Then where `main.py` is, type `pyinstaller --onefile main.py`
- A `/dist` folder will be created, in there will be an `.exe` file

## How to use:
1. When the app runs
2. Three folders will be created:
   - `Queued`
   - `Doing`
   - `Done`

## Process:
1. Put a receipt into the `Queued` folder.
2. The receipts will be processed and moved into the `Done` folder.
3. Each receipt will be grouped in its respective folder, labeled by the date and time the process completes. The original receipt can also be found here.
