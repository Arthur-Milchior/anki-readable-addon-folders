# Having readable add-on folder
## Rationale
The add-ons folder contains one folder by add-on. Each folder's name
is a string of digit. This is quite horrible for a human who want to
go read or edit the code of an add-on.

Thus, this add-on create another folder, containing symlinks with the
name of the add-on to the add-on folder.

## Warning
This does not work on windows. Because this add-ons create symbolic
links, and windows can't create them without admin privilege.

## Usage
Install this add-on and start anki. That's all. The symlinks are
created while anki start. If you install a new add-on, it's symlink
won't be created untill you restart anki.

Note also that symlinks are not deleted. Thus a symlink may break if
you delete an add-on. (TODO: change that ?)

## Configuration
By default the new folder is in the same folder than the original
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
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](https://Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
