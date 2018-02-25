import sys
import os
import operator
import re


class SongCalc():
    def abort(msg: str):
        print(msg)
        print('Aborting')
        sys.exit()

    def zipf(line_num):
        if line_num > 0:
            ret = 1 / line_num
            return ret

    def quality(playcnt, zpos):
        if zpos > 0:
            ret = playcnt / zpos
            return ret

    def get_file_path(file_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = dir_path + '/' + file_name
        if not os.path.isfile(file_path):
            SongCalc.abort('File not found: ' + file_path)
        return file_path

    def get_line_count(file_path):
        line_count = len(open(file_path).readlines())
        if line_count < 1 or line_count > 50000:
            SongCalc.abort('Linecount must be from 1 to 50,000')
        return line_count

    def get_songdata(songdata):
        file_path = SongCalc.get_file_path(songdata)
        line_count = SongCalc.get_line_count(file_path)
        lines = []
        line_num = 1
        first_line = True
        num_select = 0
        with open(file_path, "rt") as in_file:
            for line in in_file:
                tmp_line = line.rstrip('\n').split(',')
                if first_line is True:
                    num_songs = int(tmp_line[0])
                    num_select = int(tmp_line[1])
                    if num_songs < 1 or num_songs > 50000:
                        SongCalc.abort('Number of songs must be from 1 to 50,000')
                    if num_select < 1 or num_select > line_count:
                        SongCalc.abort('Number to select must be from 1 to ' + str(line_count))
                    first_line = False
                    continue
                play_count = int(tmp_line[0])
                song_name = tmp_line[1]
                if play_count < 0 or play_count > 10 ** 12:
                    SongCalc.abort('Play count must be from 0 to 10^12')
                if len(song_name) > 30:
                    SongCalc.abort('Song name must be no longer than 30 characters')
                if re.search(r'[^a-z0-9_]', song_name):
                    SongCalc.abort('Song name must only contain a-z 0-9 or an underscore (_).')
                tmp_line.insert(0, line_num)
                z_num = SongCalc.zipf(line_num)
                tmp_line.append(z_num)
                tmp_line.append(SongCalc.quality(int(tmp_line[1]), z_num))
                line_num += 1
                lines.append(tmp_line)
            lines.sort(key=operator.itemgetter(3, 0))
            return lines, num_select
