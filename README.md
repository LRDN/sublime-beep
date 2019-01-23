Beep
====

Sublime Text 3 plugin (macOS only) that plays the system alert sound whenever the end of the undo/redo stack has been reached through its custom key commands.

Installation
------------

Clone this repository into your packages directory.

```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
git clone https://github.com/lrdn/sublime-beep.git Beep
```

Configuration
-------------

Remap the undo/redo key bindings in your user settings.

```
[
	{ "keys": ["super+z"], "command": "undo_beep" },
	{ "keys": ["super+shift+z"], "command": "redo_beep" }
]
```