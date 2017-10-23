# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()
# -*- mode: python -*-

from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401
import keys


config = config  # type: ConfigAPI # noqa: F821
c = c  # type: ConfigContainer # noqa: F821

# ui
c.completion.scrollbar.width = 0
c.tabs.position = 'top'
c.tabs.show = 'always'
c.tabs.favicons.show = True
c.tabs.width.indicator = 0
c.tabs.title.format = '{title}'
c.tabs.title.alignment = 'center'
c.downloads.position = 'bottom'
c.tabs.favicons.show = True
c.scrolling.smooth = True
c.colors.webpage.bg = '#282c34'
c.completion.height = '20%'
c.statusbar.hide = True
c.hints.uppercase = True
c.downloads.remove_finished = 1
c.content.user_stylesheets = 'solarized-all-sites-dark.css'
c.downloads.open_dispatcher = 'nautilus'

# behavior

keys.bind(config)

c.downloads.location.prompt = True
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}',
                       'y': 'https://youtube.com/results?search_query={}',
                       'r': 'https://reddit.com/r/{}',
                       'rp': 'https://redditp.com/r/{}',
                       'k': 'https://kickass.cd/search.php?q={}',
                       's': 'https://soundcloud.com/search?q={}',
                       'i': 'http://www.imdb.com/find?ref_=nv_sr_fn&q=+{}&s=all',
                       'a': 'https://wiki.archlinux.org/index.php?search={}',
                       'l': 'http://libgen.io/search.php?req={}'}
c.input.insert_mode.auto_load = False
c.input.insert_mode.auto_leave = False
c.tabs.background = True
c.editor.command = ['emacsclient', '{}']
c.auto_save.session = True

theme = {
    'panel': {
        'height': 24,
    },

    'fonts': {
        'main': 'Roboto Mono Medium',
        'tab_bold': True,
        'tab_size': 12,
    },

    'colors': {
        'bg': {
            'normal': '#272b33',
            'active': '#383c4a',
            'inactive': '#2f343f',
        },

        'fg': {
            'normal': '#f3f4f5',
            'active': '#f3f4f5',
            'inactive': '#878E7D',

            # completion and hints
            'match': '#2f343f',
        },
    }
}

# colors
colors = theme['colors']


def setToBG(colortype, target):
    config.set('colors.' + target, colors['bg'][colortype])


def setToFG(colortype, target):
    config.set('colors.' + target, colors['fg'][colortype])


def colorSync(colortype, setting):
    if setting.endswith('.fg'):
        setToFG(colortype, setting)
    elif setting.endswith('.bg'):
        setToBG(colortype, setting)
    elif setting.endswith('.top') or setting.endswith('.bottom'):
        setToFG(colortype, setting)
    else:
        setToFG(colortype, setting + '.fg')
        setToBG(colortype, setting + '.bg')


targets = {
    'normal': [
        'statusbar.normal',
        'statusbar.command',
        'tabs.even',
        'tabs.odd',
        'hints',
        'downloads.bar.bg',
        ],

    'active': [
        'tabs.selected.even',
        'tabs.selected.odd',
        'statusbar.insert',
        'downloads.stop',
        'prompts',
        'messages.warning',
        'messages.error',

        'completion.item.selected',

        'statusbar.url.success.http.fg',
        'statusbar.url.success.https.fg',

        'completion.category',
    ],

    'inactive': [
        'tabs.even',
        'tabs.odd',
        'completion.scrollbar',
        'downloads.start',
        'messages.info',
        'completion.fg',
        'completion.odd.bg',
        'completion.even.bg',

        'completion.category.border.top',
        'completion.category.border.bottom',
        'completion.item.selected.border.top',
        'completion.item.selected.border.bottom',
    ],

    'match': [
        'completion.match.fg',
        'hints.match.fg',
    ]
}

for colortype in targets:
    for target in targets[colortype]:
        colorSync(colortype, target)

setToFG('active', 'statusbar.progress.bg')

config.set('hints.border', '1px solid ' + colors['fg']['normal'])


# tabbar
def makePadding(top, bottom, left, right):
    return {'top': top, 'bottom': bottom, 'left': left, 'right': right}


# TODO improve this logic
# assume height of font is ~10px, pad top by half match panel height
surround = round((theme['panel']['height'] - 10) / 2)
c.tabs.padding = makePadding(surround, surround, 8, 8)
c.tabs.indicator_padding = makePadding(0, 0, 0, 0)

# fonts
c.fonts.monospace = theme['fonts']['main']
c.fonts.completion.entry = theme['fonts']['main']
c.fonts.completion.category = theme['fonts']['main']
c.fonts.debug_console = theme['fonts']['main']
c.fonts.downloads = theme['fonts']['main']
c.fonts.hints = theme['fonts']['main']
c.fonts.keyhint = theme['fonts']['main']
c.fonts.messages.error = theme['fonts']['main']
c.fonts.messages.info = theme['fonts']['main']
c.fonts.messages.warning = theme['fonts']['main']
c.fonts.prompts = theme['fonts']['main']
c.fonts.statusbar = theme['fonts']['main']

tabFont = str(theme['fonts']['tab_size']) + 'pt ' + theme['fonts']['main']
if theme['fonts']['tab_bold']:
    tabFont = 'bold ' + tabFont

c.fonts.tabs = tabFont
