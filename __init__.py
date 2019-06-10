from anki.utils import isWin
import sys

if isWin:
    from . import readableAddons
else:
    print(f"""I beg your pardon. Currently the add-on "Add-on folder with readable names" does not work on windows. This is because this add-on is used to create symbolic links, and they can't be created without admin privilege on windows. You may want to uninstall add-on 519936472.""", sys.stderr)
