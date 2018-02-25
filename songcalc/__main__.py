import sys
import click
from .songcalc import SongCalc

sys.tracebacklimit = 0


@click.command()
@click.argument('songdata')
def main(songdata):
    lines, num_select = SongCalc.get_songdata(songdata)
    x = 0
    for line in lines:
        while x < num_select:
            print(line[2])
            x += 1
            break
    if __name__ == '__main__':
        main()
