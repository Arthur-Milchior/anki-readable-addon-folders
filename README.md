# Having readable add-on folder
## Rationale
The add-ons folder contains one folder per add-on. Each folder's name
is a string of digits. This is quite horrible for a human who wants to
go read or edit the code of an add-on.

Thus, this add-on creates another folder containing symlinks (directory 
junctions on Windows) with the name of an add-on pointing to that add-on
folder.

## Usage
Install this add-on and start Anki. That's all. The symlinks are
created while Anki starts. If you install a new add-on, its symlink
won't be created until you restart Anki.

## Configuration
By default, the new folder is in the same folder as the original
addons directory. You can change this directory in newFolder.

The name of the new folder, by default, is "namedAddons", it can also
be changed.

## Version 2.0
None

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-readable-addons-folders
Addon number| [519936472](https://ankiweb.net/shared/info/519936472)
