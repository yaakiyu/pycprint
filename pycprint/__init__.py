# pycprint by yaakiyu

from typing import Optional

__author__ = "yaakiyu"
__version__ = "0.1"

END             = '\033[0m'
BOLD            = '\033[1m'
INDISTINCT      = '\033[2m'
ITALIC          = '\033[3m'
UNDERLINE       = '\033[4m'
REVERSE         = '\033[7m'
INVISIBLE       = '\033[8m'
BLACK           = '\033[30m'
RED             = '\033[31m'
GREEN           = '\033[32m'
YELLOW          = '\033[33m'
BLUE            = '\033[34m'
MAGENTA         = '\033[35m'
CYAN            = '\033[36m'
WHITE           = '\033[37m'
BG_BLACK        = '\033[40m'
BG_RED          = '\033[41m'
BG_GREEN        = '\033[42m'
BG_YELLOW       = '\033[43m'
BG_BLUE         = '\033[44m'
BG_MAGENTA      = '\033[45m'
BG_CYAN         = '\033[46m'
BG_WHITE        = '\033[47m'
GRAY            = '\033[90m'
BEIGE           = '\033[91m'
LIGHT_GREEN     = '\033[92m'
LIGHT_YELLOW    = '\033[93m'
LIGHT_BLUE      = '\033[94m'
LIGHT_MAGENTA   = '\033[95m'
LIGHT_CYAN      = '\033[96m'
BG_GRAY         = '\033[100m'
BG_BEIGE        = '\033[101m'
BG_LIGHT_GREEN  = '\033[102m'
BG_LIGHT_YELLOW = '\033[103m'
BG_LIGHT_BLUE   = '\033[104m'
BG_LIGHT_MAGENTA= '\033[105m'
BG_LIGHT_CYAN   = '\033[106m'

def black(*content):
    return print(BLACK, *content, END, sep='')

def red(*content):
    return print(RED, *content, END, sep='')

def green(*content):
    return print(GREEN, *content, END, sep='')

def yellow(*content):
    return print(YELLOW, *content, END, sep='')

def blue(*content):
    return print(BLUE, *content, END, sep='')

def purple(*content):
    return print(MAGENTA, *content, END, sep='')

def cyan(*content):
    return print(CYAN, *content, END, sep='')

def white(*content):
    return print(WHITE, *content, END, sep='')

def bold(*content):
    return print(BOLD, *content, END, sep='')

def underline(*content):
    return print(UNDERLINE, *content, END, sep='')

def invisible(*content):
    return print(INVISIBLE, *content, END, sep='')

def reverse(*content):
    return print(REVERSE, *content, END, sep='')

def color(red: Optional[int] = 0, green: Optional[int] = 0, blue: Optional[int] = 0):
    "Returns the color escape code that you want to get by RGB."
    return f'\033[38;2;{red};{green};{blue}m'

def background_color(red: Optional[int] = 0, green: Optional[int] = 0, blue: Optional[int] = 0):
    "Returns the background-color escape code that you want to get by RGB."
    return f'\033[48;2;{red};{green};{blue}m'

def bg_color(r=0,g=0,b=0):
    "The alias of `background_color()`."
    return background_color(r,g,b)
