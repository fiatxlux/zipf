
""" List files in a directory that match a given extension"""

import argparse
import glob



def my_ls(dir, ext):
    f = glob.glob(f'{dir}/*.{ext}')
    [print(fi) for fi in f]
    return f


def main(args):
    my_ls(args.dir, args.ext)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dir', type=str, help='Input directory path')
    parser.add_argument('ext',type=str, help='File extension name e.g txt sh')
    args = parser.parse_args()
    main(args)
