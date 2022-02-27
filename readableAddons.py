import json
import os
import os.path
import sys

from aqt import mw

from .config import getNewFolder

original_folder = mw.pm.addonFolder()
new_folder = getNewFolder()

if not os.path.exists(new_folder):
    try:
        os.makedirs(new_folder)
    except PermissionError:
        msg = (
            "There is an error with the configuration of the addon"
            '"Add-on folder with readable names". Currently, it asks '
            f"to use directory {original_folder}, and you don't have the "
            "permissions to create a folder there. So, either you should "
            "change the permission of this folder, or you should select "
            "another folder."
        )
        print(msg, sys.stderr)

for entry in os.listdir(original_folder):
    original_addon_dir = os.path.join(original_folder, entry)
    if os.path.isdir(original_addon_dir):
        meta_file = os.path.join(original_addon_dir, "meta.json")
        if os.path.exists(meta_file):
            with open(meta_file, "r") as f:
                j = json.load(f)
                if "name" not in j:
                    continue
                name = j["name"]
                name = name.replace("/", "_")
        else:
            name = entry
        new_addon_dir = os.path.join(new_folder, name)
        if not os.path.exists(new_addon_dir):
            os.symlink(original_addon_dir, new_addon_dir)
