import os
import os.path
import json
from aqt import mw
from .config import getNewFolder


def debug(*args,**kwargs):
    #print(*args,**kwargs)
    pass

originalFolder = mw.pm.addonFolder()
newFolder = getNewFolder()
if not os.path.exists(newFolder):
    os.makedirs(newFolder)

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
