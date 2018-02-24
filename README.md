# savant

Song Popularity Problem

-To Install songcalc on a python 3 ready system, use install.sh

songcalc --help
Usage: songcalc [OPTIONS] SONGDATA

Options:
  --help  Show this message and exit.

ex: songcalc album1.dat

The first line of the album file contains 2 values
Number of Songs, Number to select

Number of Songs must be between 1 and 50,000
Number to Select must be between 0 and the Number of Songs selected

The subsequent lines in the album file also contain 2 values
Play Count, Song Name

Play Count must be between 0 and 50,000
The Song name must be no longer than 30 characters and only use a-z 0-9 and underscore (_).
