import os
import os.path
import json
from aqt import mw
from .config import getNewFolder
import sys


def debug(*args,**kwargs):
    #print(*args,**kwargs)
    pass

originalFolder = mw.pm.addonFolder()
newFolder = getNewFolder()
if not os.path.exists(newFolder):
    try:
        os.makedirs(newFolder)
    except PermissionError:
        print(f"""There is an error with the configuration of the addon "Add-on folder with readable names". Currently, it asks to use directory {originalFolder}, and you don't have the permissions to create a folder there. So, either you should change the permission of this folder, or you should select another folder.""", sys.stderr)

for fileName in os.listdir(originalFolder):
    originalAddonDir = os.path.join(originalFolder,fileName)
    if os.path.isdir(originalAddonDir):
        metaFile = os.path.join(originalAddonDir,"meta.json")
        if os.path.exists(metaFile):
            with open(metaFile,"r") as f:
                j = json.load(f)
                if "name" not in j:
                    continue
                name = j["name"]
        else:
            name = fileName
        newAddonDir = os.path.join(newFolder,name)
        debug(f"symlink({originalAddonDir}, {newAddonDir})")
        if not os.path.exists(newAddonDir):
            os.symlink(originalAddonDir, newAddonDir)
