import os
import argparse
import matplotlib.pyplot as plt


statistics = {'ship': [], 'small-vehicle': [], 'harbor': [], 'large-vehicle': [],
              'soccer-ball-field': [], 'ground-track-field': [], 'tennis-court': [],
              'plane': [], 'helicopter': [], 'roundabout': [], 'baseball-diamond': [],
              'bridge': [], 'swimming-pool': [], 'basketball-court': [], 'storage-tank': []}

def main(args):
    input_dir = args.input_dir
    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for name in os.listdir(input_dir):
        i = os.path.join(input_dir, name)
        # o = os.path.join(output_dir, name)
        with open(i, 'r') as fin:
            line = fin.readline()
            line = fin.readline()
            line = fin.readline()
            while line:
                line = line.split(' ')
                cls = line[-2:-1][0]
                xs = [int(n) for n in line[0:7:2]]
                ys = [int(n) for n in line[1:8:2]]
                xmin = min(xs)
                xmax = max(xs)
                ymin = min(ys)
                ymax = max(ys)
                vol = (ymax - ymin) * (xmax - xmin)
                statistics[cls].append(vol)
                line = fin.readline()
                # xmin, ymin, xmax, ymax
    for k in statistics.keys():
        plt.hist(statistics[k], bins=100)
        axis = plt.gca()
        axis.set_title(k)
        # plt.show()
        plt.savefig(os.path.join(output_dir, k + '.png'))
        plt.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate HBB from OBB")
    parser.add_argument('--input_dir', '-i', default='/home/yqi/Desktop/train/labelTxt', help='OBB annotation direction')
    parser.add_argument('--output_dir', '-o', default='statistics', help='output direction')
    args = parser.parse_args()
    main(args)
