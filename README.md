## Introduction
Panterfish is a fork of sunfish, a simple, but strong chess engine, written in Python.

# Play against panterfish!

The simplest way to run panterfish is through the "fancy" terminal interface:
<pre>
$ <b>tools/fancy.py -cmd ./panterfish.py</b>
Playing against ...
Do you want to be white or black? <b>black</b>
  1 ♖ ♘ ♗ ♔ ♕ ♗ ♘ ♖
  2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
  3
  4
  5
  6
  7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
  8 ♜ ♞ ♝ ♚ ♛ ♝ ♞ ♜
    h g f e d c b a

Score: 23, nodes: 11752, nps: 13812, time: 0.9
 My move: d4
  1 ♖ ♘ ♗ ♔ ♕ ♗ ♘ ♖
  2 ♙ ♙ ♙ ♙   ♙ ♙ ♙
  3
  4         ♙
  5
  6
  7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
  8 ♜ ♞ ♝ ♚ ♛ ♝ ♞ ♜
    h g f e d c b a

Your move (e.g. c6 or g8h6): <b>Nf6</b>
</pre>

Note this requires the [python-chess](https://github.com/niklasf/python-chess/) package.
For a true minimalist experience, first we can "pack" panterfish into a compressed executable (less than 3KB!) and run it directly:
<pre>
$ <b>build/pack.sh panterfish.py packed.sh</b>
Total length: 2953
$ <b>./packed.sh</b>
<b>go wtime 1000 btime 1000 winc 1000 binc 1000</b>
info depth 1 score cp 0 pv d2d4
bestmove d2d4
</pre>
(See the [UCI specification](http://wbec-ridderkerk.nl/html/UCIProtocol.html) for the full set of commands.)

### Playing with a graphical interface

It is also possible to run panterfish with a graphical interface, such as [PyChess](http://pychess.org) or [Arena](http://www.playwitharena.de).

Finally you can [play panterfish now on Lichess](https://lichess.org/@/panterfish-engine)


# Features

1. Built around the simple, but efficient MTD-bi search algorithm, also known as [C*](https://www.chessprogramming.org/NegaC*).
2. Filled with classic "chess engine tricks" for simpler and faster code.
3. Efficiently updatedable evaluation function through [Piece Square Tables](https://www.chessprogramming.org/Piece-Square_Tables).
4. Uses standard Python collections and data structures for clarity and efficiency.

# Limitations

panterfish supports all chess rules, except the 50 moves draw rule.

There are many ways in which you may try to make panterfish stronger. First you could change from a board representation to a mutable array and add a fast way to enumerate pieces. Then you could implement dedicated capture generation, check detection and check evasions. You could also move everything to bitboards, implement parts of the code in C or experiment with parallel search!

The other way to make panterfish stronger is to give it more knowledge of chess. The current evaluation function only uses piece square tables - it doesn't even distinguish between midgame and endgame. You can also experiment with more pruning - currently only null move is done - and extensions - currently none are used. Finally panterfish might benefit from a more advanced move ordering, MVV/LVA and SEE perhaps?

An easy way to get a strong panterfish is to run with with the [PyPy Just-In-Time intepreter](https://pypy.org/). In particular the python2.7 version of pypy gives a 250 ELO boost compared to the cpython (2 or 3) intepreters at fast time controls:

    Rank Name                    Elo     +/-   Games   Score   Draws
       1 pypy2.7 (7.1)           166      38     300   72.2%   19.7%
       2 pypy3.6 (7.1)            47      35     300   56.7%   21.3%
       3 python3.7               -97      36     300   36.3%   20.7%
       4 python2.7              -109      35     300   34.8%   24.3%


# Why panterfish?

The name panterfish actually refers to the [Pygmy panterfish](http://en.wikipedia.org/wiki/Pygmy_panterfish), which is among the very few fish to start with the letters 'Py'. The use of a fish is in the spirit of great engines such as Stockfish, Zappa and Rybka.

In terms of Heritage, panterfish borrows much more from [Micro-Max by Geert Muller](http://home.hccnet.nl/h.g.muller/max-src2.html) and [PyChess](http://pychess.org).

# License

[GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
