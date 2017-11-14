#!/usr/bin/env python
# coding=utf-8

"""
Removes old files and makes symlinks
"""

from subprocess import call
from os import listdir
from pathlib import Path

HOME    = str(Path.home()) + '/'
REPODIR = 'vimconfig/'
DEBUG   = False


def link(source, dest):
    remove = ['rm', HOME + dest]
    link   = ['ln', '-s', HOME + REPODIR + source, HOME + dest]

    if DEBUG:
        print(remove)
        print(link)
    else:
        call(remove)
        call(link)


# i3
link('i3wm/.i3rc', '.config/i3/config')
link('i3wm/compton.conf', '.config/compton.conf')
link('bg', 'bg')

# scripts
for script in listdir(HOME + REPODIR + 'scripts'):
    link('scripts/' + script, script)

# emacs
link('emacs/.emacs', '.emacs')

# qutebrowser
link('qutebrowser', '.config/qutebrowser')

# transmission
link('transmission/settings.json', '.config/transmission/settings.json')

# vim
link('vim/.vimrc', '.vimrc')
link('vim/.nvimrc', '.nvimrc')