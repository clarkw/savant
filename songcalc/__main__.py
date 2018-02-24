import sys
import click
import os
import operator
import re

@click.command()
@click.argument('songdata')

def main(songdata):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path+'/'+songdata
    lines = []
    line_num = 1
    first_line = True
    line_count = len(open(file_path).readlines())
    if line_count < 1 or line_count > 50000:
        print('Linecount must be from 1 to 50,000')
        print('Aborting')
        sys.exit();
    with open(file_path, "rt") as in_file:
        for line in in_file:
            tmp_line = line.rstrip('\n').split(',')
            if first_line is True:
                num_songs = int(tmp_line[0])
                num_select = int(tmp_line[1])
                if num_songs < 1 or num_songs > 50000:
                    print('Number of songs must be from 1 to 50,000')
                    print('Aborting')
                    in_file.close()
                    sys.exit();
                if num_select < 1 or num_select > line_count:
                    print('Number to select must be from 1 to ' + line_count)
                    print('Aborting')
                    in_file.close()
                    sys.exit();
                first_line = False
                continue

            play_count = int(tmp_line[0])
            song_name = tmp_line[1]
            if play_count < 0 or play_count > 10 ^ 12:
                print('Play count must be from 0 to 10^12')
                print('Aborting')
                in_file.close()
                sys.exit();
            if len(song_name) > 30:
                print('Song name must be no longer than 30 characters')
                print('Aborting')
                in_file.close()
                sys.exit();
            if re.search(r'[^a-z0-9_]', song_name):
                print('Song name must only contain a-z 0-9 or an underscore (_).')
                print('Aborting')
                sys.exit();
            tmp_line.insert(0, line_num)
            z_num = zipf(line_num)
            tmp_line.append(z_num)
            tmp_line.append(quality(int(tmp_line[1]), z_num))
            line_num += 1
            lines.append(tmp_line)
        lines.sort(key = operator.itemgetter(3, 0))

    in_file.close()
    x = 0
    for line in lines:
        while x < num_select:
            print(line[2])
            x+=1
            break

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
