# AutoBin (v1.0)

# Function:

1. Checks %systemdrive%\Windows\Temp and %userprofile%\AppData\Local\Temp
2. Puts all contents from those folders and places them in the recycle bin
3. Deletes contents of the recycle bin while skipping the confirmation interface.
4. Program closes.

# Problem(s):

1. Not tested or adapted for iOS or Linux.
2. Windows defender detects program as trojan

# Additional:

1. Script written with the help of GPT-3.5 and BingAI
2. Icon changed via Resource Hacker
3. .py script turned into .exe via cmd command - pyinstaller --onefile --noconsole AutoBin.py
4. .exe compiled into a setup file via InstallForge
