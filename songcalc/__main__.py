import click
import os
import operator

@click.command()
@click.argument('songdata')

def main(songdata):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    lines = []
    line_num = 1
    first_line = True
    with open(dir_path+'/'+songdata, "rt") as in_file:
        for line in in_file:
            if first_line is True:
                tmp_line = line.rstrip('\n').split(',')
                numselect = int(tmp_line[1])
                first_line = False
                continue
            tmp_line = line.rstrip('\n').split(',')
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
        while x < numselect:
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
