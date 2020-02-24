# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()
# -*- mode: python -*-

from qutebrowser.config.configfiles import ConfigAPI
from qutebrowser.config.config import ConfigContainer
import keys


config = config  # type: ConfigAPI
c = c  # type: ConfigContainer

# ui
c.completion.scrollbar.width = 0
c.tabs.position = 'top'
c.tabs.show = 'always'
c.tabs.favicons.show = 'always'
c.tabs.indicator.width = 0
c.tabs.title.format = '{current_title}'
c.tabs.title.alignment = 'center'
c.downloads.position = 'bottom'
c.scrolling.smooth = True
# c.colors.webpage.bg = '#AA1c2028'
c.colors.webpage.bg = '#272b33'
c.completion.height = '20%'
c.statusbar.hide = True
c.hints.uppercase = True
c.downloads.remove_finished = 1
c.content.user_stylesheets = ['onedark-all-sites.css']
c.content.pdfjs = True
# c.hints.chars = 'asdfjkl;'
c.hints.chars = 'asdfjkl'

# behavior

c.bindings.key_mappings = {"<Ctrl-[>": "<Escape>", "<Ctrl-6>": "<Ctrl-^>",
                           "<Ctrl-M>": "<Return>", "<Shift-Return>": "<Return>",
                           "<Enter>": "<Return>", "<Shift-Enter>": "<Return>",
                           "<Ctrl-Enter>": "<Ctrl-Return>"}
keys.bind(config)

c.downloads.location.prompt = False
c.downloads.location.directory = '~/Downloads/'
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}',
                       'y': 'https://youtube.com/results?search_query={}',
                       'r': 'https://reddit.com/r/{}',
                       'w': 'https://en.wikipedia.org/w/index.php?search={}',
                       'rp': 'https://redditp.com/r/{}',
                       'rt': 'https://www.rottentomatoes.com/search/?search={}',
                       'ra': 'https://proxyrarbg.org/torrents.php?search={}&category%5B%5D=14&category%5B%5D=48&category%5B%5D=17&category%5B%5D=44&category%5B%5D=45&category%5B%5D=47&category%5B%5D=50&category%5B%5D=51&category%5B%5D=52&category%5B%5D=42&category%5B%5D=46&category%5B%5D=18&category%5B%5D=41&category%5B%5D=49&category%5B%5D=23&category%5B%5D=25&category%5B%5D=27&category%5B%5D=28&category%5B%5D=40&category%5B%5D=32&category%5B%5D=33',
                       'k': 'https://kat.sx/usearch/{}',
                       's': 'https://soundcloud.com/search?q={}',
                       'i': 'http://www.imdb.com/find?ref_=nv_sr_fn&q=+{}&s=all',
                       'a': 'https://wiki.archlinux.org/index.php?search={}',
                       'am': 'https://www.amazon.co.uk/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}',
                       'e': 'https://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0',
                       'm': 'https://www.openstreetmap.org/search?query={}',
                       'pj': 'https://www.prisjakt.no/raw.php?query={}',
                       'g': 'https://github.com/search?utf8=%E2%9C%93&q={}&type=',
                       'l': 'http://gen.lib.rus.ec/search.php?req={}&open=0&res=25&view=simple&phrase=1&column=title',
                       'p': 'https://www.protondb.com/search?q={}',
                       'z': 'https://www.zalando.no/dame/?q={}',
                       'b': 'https://www.blush.no/search?q={}',
                       'vcv': 'https://vcvrack.com/plugins#{}'

}
c.input.insert_mode.auto_load = False
c.input.insert_mode.auto_leave = False
c.tabs.background = True
c.editor.command = ['emacsclient', '-c', '{}']
c.auto_save.session = True

theme = {
    'panel': {
        'height': 28,
    },

    'fonts': {
        'main': '12pt Roboto Slab Mono',
        'status': '10pt Roboto Slab Mono',
        'entry': '11pt Roboto Slab Mono',
        'tab_bold': True,
        'tab_size': 12,
    },

    'colors': {
        'bg': {
            'normal': '#272b33',
            'active': '#272b33',
            'inactive': '#272b33',
        },

        'fg': {
            'normal': '#f3f4f5',
            'active': '#896cad',
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
        'tabs.even',
        'tabs.odd',
        'hints',
        'downloads.bar.bg',
        ],

    'active': [
        'statusbar.normal',
        'statusbar.command',
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

surround = round((theme['panel']['height'] - 14) / 2)
c.tabs.padding = makePadding(surround, surround, 4, 4)
c.tabs.indicator.padding = makePadding(0, 0, 0, 0)

# fonts
c.fonts.monospace = theme['fonts']['main']
c.fonts.completion.entry = theme['fonts']['status']
c.fonts.completion.category = theme['fonts']['status']
c.fonts.debug_console = theme['fonts']['main']
c.fonts.downloads = theme['fonts']['main']
c.fonts.hints = theme['fonts']['status']
c.fonts.keyhint = theme['fonts']['main']
c.fonts.messages.error = theme['fonts']['main']
c.fonts.messages.info = theme['fonts']['main']
c.fonts.messages.warning = theme['fonts']['main']
c.fonts.prompts = theme['fonts']['main']
c.fonts.statusbar = theme['fonts']['entry']

tabFont = str(theme['fonts']['tab_size']) + 'pt ' + theme['fonts']['main']
if theme['fonts']['tab_bold']:
    tabFont = 'bold ' + tabFont

c.fonts.tabs = tabFont
