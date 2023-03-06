#!/usr/bin/env pypy3

import time, math

from collections import namedtuple, defaultdict

# If we could rely on the env -S argument, we could just use "pypy3 -u"
# as the shebang to unbuffer stdout. But alas we have to do this instead:
#from functools import partial
#print = partial(print, flush=True)

version = "Panterfish 2023.3"

###############################################################################
# UCI User interface
###############################################################################
import position as position

def parse(c):
    fil, rank = ord(c[0]) - ord("a"), int(c[1]) - 1
    return position.A1 + fil - 10 * rank


def render(i):
    rank, fil = divmod(i - position.A1, 10)
    return chr(fil + ord("a")) + str(-rank + 1)

hist = [position.Position(position.initial, 0, (True, True), (True, True), 0, 0)]

import sys, tools.uci
tools.uci.run(sys.modules[__name__], hist[-1])
sys.exit()