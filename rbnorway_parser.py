#!/usr/bin/env python3
# run with inputfile and outputfile as arguments
# eg. ./rbnorway_parser akuma-t7-frames akuma.json

import sys
import bs4
import json
from collections import OrderedDict

if len(sys.argv) != 3:
    raise Exception('IncorrectArguments')

with open(sys.argv[1]) as f:
    soup = bs4.BeautifulSoup(f, "html.parser")

if not bool(soup.find()):
    raise Exception('NotHtml')

things = soup.find_all('td')

frame_data = []
for thing in things:
    if not thing.contents:
        frame_data.append('-')
        continue
    if isinstance(thing.contents[0], bs4.element.NavigableString): 
        if thing.contents[0] != 'Notes':
            frame_data.append(str(thing.contents[0]))

c = 0
move = OrderedDict()
whole_thing = []
for line in frame_data:
    if line == ' ':
        line = '-'
    if c == 0:
        move["Command"] = line
    elif c == 1:
        move["Hit level"] = line
    elif c == 2:
        move["Damage"] = line
    elif c == 3:
        move["Start up frame"] = line
    elif c == 4:
        move["Block frame"] = line
    elif c == 5:
        move["Hit frame"] = line
    elif c == 6:
        move["Counter hit frame"] = line
    elif c == 7:
        if line.isspace():
            move["Notes"] = '-'
        else:
            move["Notes"] = line
        whole_thing.append(move.copy())
        move.clear()
        c = -1
    c += 1
with open(sys.argv[2], 'w') as f:
    json.dump(whole_thing, f, indent=4)

