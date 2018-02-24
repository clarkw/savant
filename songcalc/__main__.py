import sys
import click
import os
import operator
import re

sys.tracebacklimit = 0
@click.command()
@click.argument('songdata')

def main(songdata):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + '/' + songdata
    if os.path.isfile(file_path) != True:
        abort('File not found: ' + file_path)
    lines = []
    line_num = 1
    first_line = True
    line_count = len(open(file_path).readlines())
    if line_count < 1 or line_count > 50000:
        abort('Linecount must be from 1 to 50,000')
    with open(file_path, "rt") as in_file:
        for line in in_file:
            tmp_line = line.rstrip('\n').split(',')
            if first_line is True:
                num_songs = int(tmp_line[0])
                num_select = int(tmp_line[1])
                if num_songs < 1 or num_songs > 50000:
                    abort('Number of songs must be from 1 to 50,000')
                if num_select < 1 or num_select > line_count:
                    abort('Number to select must be from 1 to ' + line_count)
                first_line = False
                continue

            play_count = int(tmp_line[0])
            song_name = tmp_line[1]
            if play_count < 0 or play_count > 10 ** 12:
                abort('Play count must be from 0 to 10^12')
            if len(song_name) > 30:
                abort('Song name must be no longer than 30 characters')
            if re.search(r'[^a-z0-9_]', song_name):
                abort('Song name must only contain a-z 0-9 or an underscore (_).')
            tmp_line.insert(0, line_num)
            z_num = zipf(line_num)
            tmp_line.append(z_num)
            tmp_line.append(quality(int(tmp_line[1]), z_num))
            line_num += 1
            lines.append(tmp_line)
        lines.sort(key = operator.itemgetter(3, 0))
    x = 0
    for line in lines:
        while x < num_select:
            print(line[2])
            x += 1
            break

def abort(msg):
  print(msg)
  print('Aborting')
  sys.exit()

def zipf(line_num):
    if line_num > 0:
        ret = 1/line_num
        return ret

def quality(playcnt, zipf):
    if zipf > 0:
        ret = playcnt/zipf
        return ret

if __name__ == '__main__':
    main()
