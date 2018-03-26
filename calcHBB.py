import os
import argparse


def main(args):
    input_dir = args.input_dir
    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for name in os.listdir(input_dir):
        i = os.path.join(input_dir, name)
        o = os.path.join(output_dir, name)
        with open(i, 'r') as fin, open(o, 'w') as fout:
            line = fin.readline()
            fout.writelines(line)
            line = fin.readline()
            fout.writelines(line)
            line = fin.readline()
            while line:
                line = line.split(' ')
                xs = [int(n) for n in line[0:7:2]]
                ys = [int(n) for n in line[1:8:2]]
                cls = line[-2:]
                cls[0] = cls[0] + ' '
                xmin = min(xs)
                xmax = max(xs)
                ymin = min(ys)
                ymax = max(ys)
                loc = ['%d %d %d %d ' % (xmin, ymin, xmax, ymax)]
                line = ''.join(loc + cls)
                fout.write(line)
                line = fin.readline()
                # xmin, ymin, xmax, ymax


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate HBB from OBB")
    parser.add_argument('--input_dir', '-i', default='example/labelTxt', help='OBB annotation direction')
    parser.add_argument('--output_dir', '-o', default='example/HBBLabelTxt', help='output direction')
    args = parser.parse_args()
    main(args)
