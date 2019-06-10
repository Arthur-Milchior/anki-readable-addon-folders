from aqt import mw
import os.path

def getNewFolder():
    userOption = mw.addonManager.getConfig(__name__)
    newContainingFolder = userOption.get("containingFolder")
    newFolderName = userOption.get("newFolderName")
    if newContainingFolder is None:
        mw.pm.addonFolder()# ensure that base is set.
        newContainingFolder = mw.pm.base
        print(f"Containing folder is {newContainingFolder}")
    if newFolderName is None:
        newFolderName = "namedAddons"
    return os.path.join(newContainingFolder,newFolderName)
