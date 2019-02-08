from aqt import mw
import os.path

def getNewFolder():
    userOption = mw.addonManager.getConfig(__name__)
    newContainingFolder = userOption.get("containingFolder")
    newFolderName = userOption.get("newFolderName")
    if newContainingFolder is None:
        newContainingFolder = os.path.join(mw.pm.addonFolder(),"..")
    if newFolderName is None:
        newFolderName = "namedAddons"
    return os.path.join(newContainingFolder,newFolderName)
