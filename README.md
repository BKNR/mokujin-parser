# mokujin-parser
A parser for parsing RBNorway framedata into the form that is used by [Mokujin](https://github.com/BKNR/mokujin) Discord framebot.

This parser does the bare minimum, it doesn't download the RBNorway file for you, you have to use wget or something to get the file. Also if the character has 10 strings, throws or other funky stuff in the framedata, you have to edit them out by hand from the resulting JSON file, if you want everything to work in the bot. 
