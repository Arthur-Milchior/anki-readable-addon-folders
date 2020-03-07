import os.path

from aqt import mw


def getNewFolder():
    userOption = mw.addonManager.getConfig(__name__)
    newContainingFolder = userOption.get("containingFolder")
    newFolderName = userOption.get("newFolderName")
    if newContainingFolder is None:
        mw.pm.addonFolder()  # ensure that base is set.
        newContainingFolder = mw.pm.base
    if newFolderName is None:
        newFolderName = "namedAddons"
    return os.path.join(newContainingFolder, newFolderName)
